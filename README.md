# Stomata Calculation
The function takes as input the annotation from YOLOv8 segmentation model. In order to obtain reliable data the function can be utilized only on dataset with one class. For the function it's needed to define the directory where are the raw annotation, the directory where store the final excel dataset, the x and y dimension of the photo and the real dimension in mm2 of the photo. As output can be obtained the number of stomata for mm2, the total area in micron for mm2 and the average dimension of the stomata in micron.
