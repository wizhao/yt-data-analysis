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