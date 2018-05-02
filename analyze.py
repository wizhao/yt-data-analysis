import os
import seaborn as sb
import matplotlib as plt
import pandas as pd

class analyze:
    
    def __init__(self, dataFile):
        self.df = pd.read_csv(os.getcwd() + '\\Data\\' + dataFile, index_col=0)
        
    def histogram(self):
        print self.df.head() # will eventually produce a histogram
        