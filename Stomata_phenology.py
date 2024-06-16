import pandas as pd
import glob as glob
import pathlib
directory = r"C:\Users\Claudio\PycharmProjects\ProgettiCoding\Area and number Calculator\Raw_Data"
x_dimension = 2592
y_dimension = 1944
total_picture_area = 0.200



data_file = {}
for file in glob.glob(fr"{directory}\*.txt"):
    filename = pathlib.Path(fr"{directory}\{file}").stem
    new_file = open(file, "r")
    x_width = x_dimension
    y_width = y_dimension
    total_picture_area_pixel = x_width * y_width
    total_picture_area_mm2 = total_picture_area
    pixel_to_mm2 = total_picture_area_mm2 / total_picture_area_pixel
    number_of_stomata = 0
    total_area = 0.0
    data = []
    for line in new_file:
        annotation = line.split()
        if len(annotation) > 2:
            number_of_stomata += 1
            x = list(map(float, annotation[1::2]))
            y = list(map(float, annotation[2::2]))
            list_point_n = list(zip(x, y))
            y_real = [i * y_width for i in y]
            x_real = [i * x_width for i in x]
            list_point = list(zip(x_real, y_real))
            number_of_vertices = len(list_point)
            sum_1 = 0.0
            sum_2 = 0.0
            for i in range(0, number_of_vertices - 1):
                sum_1 += list_point[i][0] * list_point[i + 1][1]
                sum_2 += list_point[i][1] * list_point[i + 1][0]
            final_sum_1 = sum_1 + list_point[number_of_vertices - 1][0] * list_point[0][1]
            final_sum_2 = sum_2 + list_point[0][0] * list_point[number_of_vertices - 1][1]
            final_sum = round(abs((final_sum_1 - final_sum_2)) / 2, 2)
            real_area = final_sum * pixel_to_mm2
            total_area += real_area
        else:
            print(f"There was a problem with annotation: {filename}")
    area_micron = round(total_area, 6) * 1000000
    mean_stomata_area_micron = round(total_area / number_of_stomata, 6) * 1000000
    number_stomata_for_mm2 = int(number_of_stomata / total_picture_area_mm2)
    total_area_for_mm2 = (area_micron / (total_picture_area_mm2 * 1000000)) *100
    data.append(number_of_stomata)
    data.append(number_stomata_for_mm2)
    data.append(total_area_for_mm2)
    data.append(mean_stomata_area_micron)
    data_file[filename] = data

df = pd.DataFrame.from_dict(data_file, orient="index")
df.rename(columns={0: "number stomata photo", 1: "number stomata (mm2)", 2: "SPI(%)", 3: "average area (micron)"}, inplace=True)
name_file = input("How do you want to name the file?")
df.to_excel(fr"{name_file}.xlsx")





