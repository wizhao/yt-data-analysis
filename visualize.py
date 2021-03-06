import matplotlib.pyplot as plt

class visualize:
    
    def __init__(self): #do nothing on initialization
        pass
        
    def bargraph(self, dataSet): #creates bar graphs
        i = 0
        
        while i < len(dataSet): #extracts data from 5 data files
            x = []
            y = []
            names = []
            j = 0
            while (j < len(dataSet[i])): #formats data into 2 lists for plotting purposes
                short = dataSet[i][j][0]
                short = str(short)[:15]
                names.append(short)
                y.append(int(dataSet[i][j][1]))
                x.append(j+1)
                j += 1
            if i == 0:
                plt.figure(1) #create a new window
                plt.bar(x, y, color="b") #create bar graph with specific color
                plt.xticks(x,names) #add categories to data
                plt.xlabel("Channel Name") #Add labels on axes
                plt.ylabel("Frequency in Trending") #||
                plt.title("US Trending Frequency by Channel") #Add title of graph
                
            elif i ==1: #repeat for Canada and UK
                plt.figure(2)
                plt.bar(x, y, color="g")
                plt.xticks(x,names)
                plt.xlabel("Channel Name")
                plt.ylabel("Frequency in Trending")
                plt.title("CA Trending Frequency by Channel")
                
            elif i == 2:
                plt.figure(3)
                plt.bar(x, y, color="y")
                plt.xticks(x,names)
                plt.xlabel("Channel Name")
                plt.ylabel("Frequency in Trending")
                plt.title("GB Trending Frequency by Channel")
                
            i+= 1
        #show() #dont show until the end
        
    def piechart(self, dataSet):
        plt.figure(4)
        def autopct_more_than_5(pct):   #Displays percent iff it's >5%
            return ('%1.f%%' % pct) if pct > 5 else ''
        '''no worky
        def autopct_color(pct):
            colorlist = {
            "Film & Animation":"c",
            "Auto & Vehicles":"",
            "Music":"coral",
            "Pets & Animals":"",
            "Sports":"yellowgreen",
            "Short Movies":"",
            "Travel & Events":"",
            "Gaming":"",
            "Video Blogs":"",
            "People & Blogs":"purple",
            "Comedy":"r",
            "Entertainment":"royalblue",
            "News & Politics":"brown",
            "HowTo & Style":"green",
            "Education":"",
            "Science & Technology":"pink",
            "Nonprofits & Activism":"",
            "Movies":"",
            "Anime/Animation":"",
            "Action/Adventure":"",
            "Classics":"",
            "Documentary":"",
            "Drama":"",
            "Family":"",
            "Foreign":"",
            "Horror":"",
            "Sci-Fi/Fantasy":"",
            "Thriller":"",
            "Shorts":"",
            "Shows":"",
            "Trailers":""
            }
            val = int(round(pct*self.total/100.0))
            cat = labels[sizes.index(val)]
            if cat == "Other":
                return "gray"
            else:
                return colorlist[cat]
        '''
        def makelists(data): #formats data into 2 lists
            self.total = 0
            labels = []
            sizes = []
            total = 0
            for j in data:
                labels.append(j[0])
                sizes.append(j[1])
                self.total += j[1]
            return sizes,labels
        
        def makeOther(sizes,labels): #congregates small percents under 5% into the "Other" category
            other = 0
            count = 0
            for j in sizes:
                if float(j)/self.total < 0.05:
                    count += 1
                    other += j    
            if other > 0:
                sizes = sizes[:-count]
                labels = labels[:-count]
                labels.append("Other")
                sizes.append(other)
            return sizes, labels
        
        
        i=0
        while i < len(dataSet): #loops thru the 5 data tables, making a pie chart for each
            a,b = makelists(dataSet[i])
            sizes, labels = makeOther(a,b) #gets appropriate data for each chart
            if i == 0:
                plt.subplot(231) #determines the spot on the window
                plt.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1) #makes the pie chart
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title("United States") #sets title
                
            elif i == 1: #repeat for all pie charts
                plt.subplot(233)
                plt.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1)
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title("Canada")
            elif i == 2:
                plt.subplot(234)
                plt.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1)
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title("Germany")
            elif i == 3:
                plt.subplot(235)
                plt.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1)
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title("France")
            elif i == 4:
                plt.subplot(236)
                plt.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1)
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title("United Kingdom")
            i += 1
        #fp.show() #dont show until the end
        
        
        
    
    def scatterplot(self, dataSet):
        plt.figure(5)
        i=0
        while i < len(dataSet):                
            x=[]
            y=[]
            j=0
            while j < len(dataSet[i]):
                x.append(int(dataSet[i][j][0]))
                y.append(int(dataSet[i][j][1]))
                j += 1
            
            if i == 0:
                plt.subplot(232)
                plt.scatter(x, y, color="b", s=40)
                plt.xlabel('Likes')
                plt.ylabel('Dislikes')
                plt.title('US Dislikes vs Likes')
                plt.subplot(231)
                plt.scatter(x, y, label="United States", color="b", s=40)
            elif i == 1:
                plt.subplot(233)
                plt.scatter(x, y, color="g", s=40)
                plt.xlabel('Likes')
                plt.ylabel('Dislikes')
                plt.title('CA Dislikes vs Likes')
                plt.subplot(231)
                plt.scatter(x, y, label="Canada", color="g", s=40)
            elif i == 2:
                plt.subplot(234)
                plt.scatter(x, y, color="k", s=40)
                plt.xlabel('Likes')
                plt.ylabel('Dislikes')
                plt.title('GE Dislikes vs Likes')
                plt.subplot(231)
                plt.scatter(x, y, label="Germany", color="k", s=40)
            elif i == 3:
                plt.subplot(235)
                plt.scatter(x, y, color="r", s=40)
                plt.xlabel('Likes')
                plt.ylabel('Dislikes')
                plt.title('FR Dislikes vs Likes')
                plt.subplot(231)
                plt.scatter(x, y, label="France", color="r", s=40)
            else:
                plt.subplot(236)
                plt.scatter(x, y, color="y", s=40)
                plt.xlabel('Likes')
                plt.ylabel('Dislikes')
                plt.title('GB Dislikes vs Likes')
                plt.subplot(231)
                plt.scatter(x, y, label="Britain", color="y", s=40)
            i += 1
        
        plt.legend(loc="upper right")
        plt.xlabel('Likes')
        plt.ylabel('Dislikes')
        plt.title('Countries Dislikes vs Likes')
        plt.show()