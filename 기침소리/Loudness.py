import soundfile as sf
import pyloudnorm as pyln

data, rate = sf.read("file_example_WAV_1MG.wav") # load audio (with shape (samples, channels))
print(data.shape)
meter = pyln.Meter(rate) # create BS.1770 meter
loudness = meter.integrated_loudness(data) # measure loudness
print(loudness)