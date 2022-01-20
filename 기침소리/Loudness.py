import soundfile as sf
import pyloudnorm as pyln
import os

wave_dir = 'C:/Users/kimsa/Documents/SoundLAB/기침소리/mulit_waves/3901_1.0_1'

def get_wave_files(main_dir):
    wave_files = []
    for(dirpath, dirname, filenames) in os.walk(wave_dir):
        for filename in filenames:
            filename_path = os.sep.join([dirpath, filename])
            wave_files.append(filename_path)
        return wave_files

wave_files = get_wave_files(wave_dir)
loudness = []
for wave_file in wave_files:
    data, rate = sf.read(wave_file) # load audio (with shape (samples, channels))
    meter = pyln.Meter(rate, block_size=0.03) # create BS.1770 meter
    l = meter.integrated_loudness(data) # measure loudness
    if l > -100: loudness.append(l)
    else : loudness.append(0) 

scale = min(loudness)
output = []
for x in loudness:
    if x==0:
        output.append(0)
    else:
        output.append((x-scale)*0.629)
for o in output:
    print(o)