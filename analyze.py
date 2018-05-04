import visualize as vz
from collections import defaultdict as dd

class country:
     
    def __init__(self, fileName):
        self.data = vz.analyze(fileName)
       
    def channel_sort(self): #Sorts the file based on channel frequency
        channels = []
        for item in self.data.df['channel_title']:
            channels.append(item)
            
        self.sortedC = [] 
        repeat = dd(int)
        
        for item in channels:
            repeat[item] += 1
            
        for key in self.repeat:
            self.sortedC.append([key, repeat[key]])
        
        self.sortedC.sort(key=lambda x: x[1], reverse=True)
        
        return self.sortedC
    
    def category_analysis(self): #Sorts the files based on category
        categories = {
            1:"Film & Animation",
            2:"Auto & Vehicles",
            10:"Music",
            15:"Pets & Animals",
            17:"Sports",
            18:"Short Movies",
            19:"Travel & Events",
            20:"Gaming",
            21:"Video Blogs",
            22:"People & Blogs",
            23:"Comedy",
            24:"Entertainment",
            25:"News & Politics",
            26:"HowTo & Style",
            27:"Education",
            28:"Science & Technology",
            29:"Nonprofits & Activism",
            30:"Movies",
            31:"Anime/Animation",
            32:"Action/Adventure",
            33:"Classics",
            34:"Comedy",
            35:"Documentary",
            36:"Drama",
            37:"Family",
            38:"Foreign",
            39:"Horror",
            40:"Sci-Fi/Fantasy",
            41:"Thriller",
            42:"Shorts",
            43:"Shows",
            44:"Trailers",
        }