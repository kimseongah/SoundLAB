import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField
import os

#raw data 불러오기

main_dir = 'D:/Projects/Main_Code/testt' 

def get_csv_files(main_dir):
    csv_files = []
    for (dirpath, dirname, filenames) in os.walk(main_dir):
        
        for filename in filenames:
            filename_path = os.sep.join([dirpath, filename])
            csv_files.append(filename_path)                             
        return csv_files
csv_files = get_csv_files(main_dir)

#%%
#이미지로 변환
count = 0
for csv_file in csv_files:
    csv_name = csv_file.split('/')[-1].split('.')                               
    x = np.loadtxt(open(csv_file,encoding="utf-8"),delimiter=";",usecols=(1),max_rows=15).T
    # print(type(x),x.shape)
    X = x[:]
    X = X.reshape(1, -1)
    print(type(X),X.shape)
    image_size = 15
    gasf = GramianAngularField(image_size)
    X_gasf = gasf.fit_transform(X)
    print(X_gasf.shape)
    print(X_gasf[0,4,2],X_gasf[0,2,4])
    # gadf = GADF(image_size)
    # X_gadf = gadf.fit_transform(X)
    # print(X_gadf[0,1,2],X_gadf[0,2,1])
    12
    # Show the results for the first time series
    plt.figure(figsize=(16, 8))
    # plt.subplot(121)
    plt.imshow(X_gasf[0], cmap='rainbow',origin='lower')
    plt.title("GASF", fontsize=16)
    # plt.subplot(122)
    # plt.imshow(X_gadf[0], cmap='rainbow', origin='lower')
    # plt.title("GADF", fontsize=16)
    plt.savefig('D:/Projects/Main_Code/newimg'+'/'+str(count)+'.png')
    plt.close()
    count +=1

#%%
#이미지 흰 배경 자르기
from PIL import Image    
import os
maindir = 'D:/Projects/Main_Code/Parameters/Validation/testothers/a'
for parent, dirnames, filenames in os.walk(maindir):        
 for filename in filenames:
        pic_name = os.path.join(parent, filename)
        img= Image.open(pic_name)
        img=img.convert('RGB')
        caijian = img.crop((8,5,342,222))
        caijian.save('D:/Projects/Main_Code/Parameters/Validation/testothers/a/'+filename)
 