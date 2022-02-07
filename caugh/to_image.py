import numpy as np
import matplotlib.pyplot as plt
from pyts.image import GramianAngularField
from PIL import Image    
import os
import shutil

import warnings
warnings.filterwarnings('ignore')

import into_multi_wave
import Loudness


wav_file = '3901_1.0_1.wav'
multi_wav_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/mulit_waves/' #폴더를 미리 존재시켜놔야함
image_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/image/' #폴더를 미리 존재시켜놔야함

def make_image(sq):
    x = np.array(sq).T
    # print(type(x),x.shape)
    X = x[:]
    X = X.reshape(1, -1)
    # print(type(X),X.shape)
    image_size = 15
    gasf = GramianAngularField(image_size)
    X_gasf = gasf.fit_transform(X)
    # gadf = GADF(image_size)
    # X_gadf = gadf.fit_transform(X)
    # print(X_gadf[0,1,2],X_gadf[0,2,1])
    # Show the results for the first time series
    plt.figure(figsize=(16, 8))
    # plt.subplot(121)
    plt.imshow(X_gasf[0], cmap='rainbow',origin='lower')
    plt.title("GASF", fontsize=16)
    # plt.subplot(122)
    # plt.imshow(X_gadf[0], cmap='rainbow', origin='lower')
    # plt.title("GADF", fontsize=16)
    plt.savefig(image_dir+filename+'_'+'.png')
    plt.close()

f = wav_file.split('.')
filename = ''
for i in range(len(f)-1):
    if(i != len(f)-2):
        filename = filename+f[i]+'.'
    else : filename = filename+f[i]

for i in range(len(f)-1):
    if(i != len(f)-2):
        multi_wav_dir = multi_wav_dir+f[i]+'.'
    else : multi_wav_dir = multi_wav_dir+f[i]

if(os.path.isdir(multi_wav_dir)):
    shutil.rmtree(multi_wav_dir)
Loudness.makedirs(multi_wav_dir)

#wav파일 자르기
split_wav = into_multi_wave.SplitWavAudioMubin(wav_file)
split_wav.multiple_split(multi_wav_dir)

#raw data 불러오기
loudness = Loudness.get_loudness(wav_file, multi_wav_dir)

#이미지로 변환                            
make_image(loudness)

#이미지 흰 배경 자르기
# img= Image.open(image_dir+filename+'.png')
# img=img.convert('RGB')
# caijian = img.crop((8,5,342,222)) -> 값이 잘못된 것 같아요!
# caijian.save(image_dir+filename+'.png')
