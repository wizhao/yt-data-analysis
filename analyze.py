import visualize as vz
from collections import defaultdict as dd

class country:
     
    def __init__(self, fileName):
        self.data = vz.analyze(fileName)
       
    def channel_sort(self): #Sorts the file based on channel frequency
        self.channels = []
        for item in self.data.df['channel_title']:
            self.channels.append(item)
            
        self.sortedC = [] 
        self.repeat = dd(int)
        
        for item in self.channels:
            self.repeat[item] += 1
            
        for key in self.repeat:
            self.sortedC.append([key, self.repeat[key]])
        
        self.sortedC.sort(key=lambda x: x[1], reverse=True)
        
        return self.sortedC
