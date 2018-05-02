import analyze as vz
from collections import defaultdict as dd

class country:
     
    def __init__(self, fileName):
        self.data = vz.analyze(fileName)
       
    def channel_sort(self):
        channels = []
        for item in self.data.df['channel_title']:
            channels.append(item)
            
        self.sortedC = [] 
        repeat = dd(int)
        
        for item in self.channels:
            repeat[item] += 1
            
        for key in repeat:
            self.sortedC.append([key, repeat[key]])
        
        self.sortedC.sort(key=lambda x: x[1], reverse=True)
        
        return self.sortedC
