import timbral_models
from cmath import pi
import soundfile as sf
import pyloudnorm as pyln
import os

#timbral_util 1789번째줄 체크하는 부분 지우기

def get_wave_files(wave_dir):
    wave_files = []
    for(dirpath, dirname, filenames) in os.walk(wave_dir):
        for filename in filenames:
            filename_path = os.sep.join([dirpath, filename])
            wave_files.append(filename_path)
        return wave_files


def get_roughness(file, wave_dir):
    wave_files = get_wave_files(wave_dir)
    roughness= []

    for wave_file in wave_files:
         roughness.append(timbral_models.timbral_roughness(wave_file))
    return roughness

# wav_file = '3901_1.0_4.wav'
# multi_wav_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/mulit_waves/' #폴더를 미리 존재시켜놔야함
# image_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/image/' #폴더를 미리 존재시켜놔야함

# f = wav_file.split('.')
# for i in range(len(f)-1):
#     if(i != len(f)-2):
#         multi_wav_dir = multi_wav_dir+f[i]+'.'
#     else : multi_wav_dir = multi_wav_dir+f[i]

# print(get_roughness(wav_file, multi_wav_dir))