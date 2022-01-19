import matlab.engine
import numpy as np
from numpy import array, arange
from matlab import double as double_m

eng = matlab.engine.start_matlab()
eng.desktop(nargout=0)

# eng.eval("[audioIn,fs] = audioread('file_example_WAV_1MG.wav');", nargout=0)

# fluctuation = eng.eval("acousticFluctuation(audioIn,fs);")

# print(fluctuation)

data = eng.audioread('file_example_WAV_1MG.wav')
fluctuation = eng.acousticFluctuation(data[0])

print(fluctuation)