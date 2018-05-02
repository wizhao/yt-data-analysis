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
            2- Channel Name
            3- Category
            4- Publish Date
            5- Tags
            6- Views
            7- Likes
            8- Dislikes
            9- Comment Count
            '''
            self.videos[sep[0]] = [sep[2], sep[3], sep[4], sep[5], sep[6], sep[7], sep[8], sep[9]]