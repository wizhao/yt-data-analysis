import visualize as vz
import random as rand
from collections import defaultdict as dd

class country:
     
    def __init__(self, fileName): # Creates the data table from the CSV file 
        self.data = vz.visualize(fileName)
        
       
    def channel_sort(self): # Sorts the file based on channel frequency
        channels = []
        for item in self.data.df['channel_title']: # Stores all channel names
            channels.append(item)
            
        self.sortedC = [] 
        self.repeat = dd(int)
        
        for item in channels: # Counts the number of times each channel appears
            self.repeat[item] += 1
            
        for key in self.repeat: # Orders channels from increasing to decreasing frequency
            self.sortedC.append([key, self.repeat[key]])
        
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
        for item in self.data.df['category_id']: # Stores the category ID (Youtube API)
            count[item] += 1
        
        self.good = []
        for key in count: # Sets a dictionary with category frequency
            self.good.append([key, count[key]])
        
        self.good.sort(key=lambda x: x[1], reverse=True) # Sorts frequency from increasing to decreasing
        
        for i in self.good: # Replaces category IDs with category name
            i[0] = categories[i[0]]
            
        return self.good
    
    def likes_dislikes_comments(self):
        likes = []
        dislikes = []
        comments = []
        
        for item in self.data.df['likes']:
            likes.append(item)
        
        for item in self.data.df['dislikes']:
            dislikes.append(item)
        
        for item in self.data.df['comments']:
            comments.append(item)
        
        self.combined = [likes, dislikes, comments]
        return self.combined
        
    def makePieChart(self):
        self.data.piechart(self.category_analysis())
        
    def makeBarGraph(self):
        top10 = self.channel_sort()
        top10[:10]
        self.data.bargraph(top10)
    
    def makeScatterPlot(self):
        indexes = rand.sample(range(len(self.combined[0])), 50)
        self.dataset = []
        for index in indexes:
            self.dataset.append([self.combined[0][index], self.combined[1][index], self.combined[2][index]])