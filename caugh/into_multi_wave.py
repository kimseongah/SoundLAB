from pydub import AudioSegment
import math

class SplitWavAudioMubin():
    def __init__(self, filename):
        self.filename = filename
        self.audio = AudioSegment.from_wav(self.filename)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 30 #0
        t2 = to_min * 30 #30
        #print("["+str(t1)+", "+str(t2)+"]")
        split_audio = self.audio[t1:t2]
        split_audio.export(split_filename, format="wav")
        
    def multiple_split(self, dirname):
        total_mins = math.ceil(self.get_duration() // 0.030) #음원 길이//60 했던 게 split이 1일 때 1분의 개수   
        min_per_split = 1
        for i in range(0, total_mins, min_per_split): #두자리수까지만 나온다고 생각
            if(i//10 == 0) : split_fn = dirname+'/'+'0'+str(i)+".wav"
            else : split_fn = dirname+'/'+str(i)+".wav"
            self.single_split(i, i+min_per_split, split_fn) #0,1
            # if i == total_mins - min_per_split:
            #     print('All splited successfully')

