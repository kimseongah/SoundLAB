import os
import timbral_models
import numpy as np
def timbral_loudness(fname, dev_output=False, phase_correction=False, clip_output=False, fs=0):
    audio_samples, fs = timbral_models.timbral_util.file_read(fname, fs, phase_correction=phase_correction)

    # window the audio file into 4096 sample sections
    windowed_audio = timbral_models.timbral_util.window_audio(audio_samples, window_length=1000)

    windowed_sharpness = []
    windowed_rms = []
    for i in range(windowed_audio.shape[0]):
        samples = windowed_audio[i, :]

        # calculate the rms and append to list
        windowed_rms.append(np.sqrt(np.mean(samples * samples)))

        # calculate the specific loudness
        N_entire, N_single = timbral_models.timbral_util.specific_loudness(samples, Pref=100.0, fs=fs, Mod=0)
        windowed_sharpness.append(N_entire)
    return np.average(windowed_sharpness)

def get_wave_files(wave_dir):
    wave_files = []
    for(dirpath, dirname, filenames) in os.walk(wave_dir):
        for filename in filenames:
            filename_path = os.sep.join([dirpath, filename])
            wave_files.append(filename_path)
        return wave_files


def get_loudness(file, wave_dir):
    wave_files = get_wave_files(wave_dir)
    sharpness= []

    for wave_file in wave_files:
        s = timbral_loudness(wave_file)
        # if s > -50:
        #     sharpness.append(s)
        # else :
        #      sharpness.append(0)
        sharpness.append(s)
    print(sharpness)
    return sharpness

wav_file = '3901_1.0_4.wav'
multi_wav_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/mulit_waves/' #폴더를 미리 존재시켜놔야함
image_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/image/' #폴더를 미리 존재시켜놔야함

f = wav_file.split('.')
for i in range(len(f)-1):
    if(i != len(f)-2):
        multi_wav_dir = multi_wav_dir+f[i]+'.'
    else : multi_wav_dir = multi_wav_dir+f[i]
loudness = get_loudness(wav_file, multi_wav_dir)
scale = 36.495
for x in loudness:
    if x<=0:
        print(0)
    else:
        print(x-scale)
print()