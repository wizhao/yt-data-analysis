import os
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

class visualize:
    
    def __init__(self, dataFile):
        self.df = pd.read_csv(os.getcwd() + '\\Data\\' + dataFile, index_col=0)
        
    def histogram(self):
        print self.df.head() # will eventually produce a histogram
        
        
    def piechart(self, dataSet):
        labels = []
        sizes = []
        for i in dataSet:
            labels.append(i[0])
            sizes.append(i[1])
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()