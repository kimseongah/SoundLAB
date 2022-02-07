import crepe
from scipy.io import wavfile

sr, audio = wavfile.read('3901_1.0_1.wav')
time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=True)
print(frequency)
print(confidence)
print(activation)
