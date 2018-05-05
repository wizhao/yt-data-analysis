import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class visualize:
    
    def __init__(self, dataFile):
        self.df = pd.read_csv(os.getcwd() + '\\Data\\' + dataFile, index_col=0)
        
    def histogram(self):
        print self.df.head() # will eventually produce a histogram
        
        
    def bargraph(self, dataSet):
        sns.set_style("whitegrid")
        #snsData = sns.load_dataset("tips")
        numbers = []
        channels = []
        for i in dataSet:
            channels.append(i[0])
            numbers.append(i[1])
        x_pos = [i for i, _ in enumerate(channels)]
        
        plt.bar(x_pos,numbers)
        plt.show()
        
    def piechart(self, dataSet):
        labels = []
        sizes = []
        total = 0
        for i in dataSet:
            labels.append(i[0])
            sizes.append(i[1])
            total += i[1]
        
        other = 0
        for i in range(len(sizes)):
            if float(sizes[i])/total < 0.05:
                del labels[i]
                other += sizes[i]
                del sizes[i]
                i = i-1
        
        if other > 0:
            labels.append("Other")
            sizes.append(other)
                
        
        def autopct_more_than_5(pct):
            return ('%1.f%%' % pct) if pct > 5 else ''
        '''
        def autolbl_more_than_5(pct):
            return labels[i] if pct > 5 else ''
        '''
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.3)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()