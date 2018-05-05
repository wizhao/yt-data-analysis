import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class visualize:
    
    def __init__(self, dataFile):
        self.df = pd.read_csv(os.getcwd() + '\\Data\\' + dataFile, index_col=0)
        
    def histogram(self):
        print self.df.head() # will eventually produce a histogram
        
        
    def bargraph(self, dataSet):
        '''
        sns.set_style("whitegrid")
        #snsData = sns.load_dataset("tips")
        numbers = []
        channels = []
        for i in dataSet:
            channels.append(i[0])
            numbers.append(i[1])
        ax = sns.barplot(x="Channel", y="Number of Days Trending", data=numbers, order=channels)
        #ax = sns.barplot(data=self.df.repeat)
        ax.show()
        '''
        sns.set_style("whitegrid")
        tips = sns.load_dataset("tips")
        ax = sns.barplot(x="day", y="total_bill", data=tips)
        ax.show()
    
    def piechart(self, dataSet):
        labels = []
        sizes = []
        for i in dataSet:
            labels.append(i[0])
            sizes.append(i[1])
        sizes
        
        def autopct_more_than_5(pct):
            return ('%1.f%%' % pct) if pct > 5 else ''
        
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct=autopct_more_than_5,
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()
    
    def scatterplot(self, dataSet):
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