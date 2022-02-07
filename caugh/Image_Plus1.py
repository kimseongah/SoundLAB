
import numpy as np
import os
import matplotlib.image as mp
# from skimage import img_as_ubyte
from PIL import Image
import cv2

#Mel
png_path1 = "D:/Projects/Main_Code/By RT/0.5/0.5_g/"
#SQ
png_path2 = "D:/Projects/Main_Code/Parameters/0.5/GAF/o/g/Loudness/"


savepath = "D:/Projects/Main_Code/Parameters/Training/Loudness/0.5_mix/g/"


filelist1 = os.listdir(png_path1) 
filelist2 = os.listdir(png_path2)

total_num = len(filelist1)

for i in range(total_num):
    png1 = png_path1 + str(i + 1) + '.png' 
    png2 = png_path2 + str(i + 1) + '.png'

    image1 = cv2.imread(png1)
    image1 = cv2.resize(image1, (280,280))
    image2 = cv2.imread(png2)

    image2 = cv2.resize(image2, (280,280))

    outputImage = cv2.addWeighted(image1,1,image2,0.8,0)
    # result_picture = Image.fromarray(im3)
    savepicture_name = savepath + str(i+1) + '.png' 
    # outputImage.save(savepicture_name)  
    cv2.imwrite(savepicture_name,outputImage)
    
    # GAF 이미지 + By Rt 합치기