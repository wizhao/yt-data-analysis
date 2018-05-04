import visualize as vz
from itertools import izip
from collections import defaultdict as dd

class country:
     
    def __init__(self, fileName):
        self.data = vz.visualize(fileName)
        
       
    def channel_sort(self): #Sorts the file based on channel frequency
        channels = []
        for item in self.data.df['channel_title']:
            channels.append(item)
            
        self.sortedC = [] 
        repeat = dd(int)
        
        for item in channels:
            repeat[item] += 1
            
        for key in repeat:
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
        
        count = dd(int)
        for item in self.data.df['category_id']:
            count[item] += 1
        
        self.good = []
        for key in count:
            self.good.append([key, count[key]])
        
        self.good.sort(key=lambda x: x[1], reverse=True)
        
        for i in self.good:
            i[0] = categories[i[0]]
            
        return self.good
        
    def makePieChart(self):
        self.data.piechart(self.category_analysis())