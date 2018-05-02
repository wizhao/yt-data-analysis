import os
import defaultdict

class country:
    
    self.videos = defaultdict(lambda: "NA")
    
    def __init__(fileName):
        self.fileName = fileName
    
    def makeList(self, fileName):
        os.chdir(os.getcwd() + "\\data")
        f = open(fileName, "r")
        for line in f:
            sep = line.split(",")
            '''
            0- Video ID 
            1- Channel Name
            2- Category
            3- Publish Date
            4- Tags
            5- Views
            6- Likes
            7- Dislikes
            8- Comment Count
            '''
            self.videos[sep[0]] = [sep[1], sep[2], sep[3], sep[4], sep[5], sep[6], sep[7], sep[8]]