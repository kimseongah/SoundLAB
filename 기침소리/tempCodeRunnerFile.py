wav_file = '3901_1.0_4.wav'
multi_wav_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/mulit_waves/' #폴더를 미리 존재시켜놔야함
image_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/image/' #폴더를 미리 존재시켜놔야함

f = wav_file.split('.')
for i in range(len(f)-1):
    if(i != len(f)-2):
        multi_wav_dir = multi_wav_dir+f[i]+'.'
    else : multi_wav_dir = multi_wav_dir+f[i]

print(get_sharpness(wav_file, multi_wav_dir))