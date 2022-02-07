
import librosa
import matplotlib.pyplot as plt
import librosa.display
import os
import numpy as np
# import tensorflow as tf
from matplotlib import cm
#%%
main_dir = 'D:/Projects/Main_Code/Sound/' # 音频源文件所在的文件路径

def get_wav_files(main_dir):
    wav_files = []
    for (dirpath, dirname, filenames) in os.walk(main_dir):
        for filename in filenames:
            filename_path = os.sep.join([dirpath, filename])
            wav_files.append(filename_path)
        return wav_files
wav_files = get_wav_files(main_dir)
#%%
for wav_file in wav_files:
    image_name = wav_file.split('/')[-1].split('.')[0]
    y,sr = librosa.load(wav_file, sr = None)
    melspec = librosa.feature.melspectrogram(y=y, sr=sr)
    logmelspec = librosa.power_to_db(melspec)
    plt.figure(figsize = (30,30))
    librosa.display.specshow(logmelspec, sr= sr,  x_axis='time',y_axis='mel', cmap=cm.jet)
    plt.xlim((0,180))
    plt.savefig('D:/Projects/Main_Code/rr'+'/'+str(image_name)+'.png') # 转换成图片之后要保存的文件路径
    plt.close()
                             