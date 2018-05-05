import matplotlib.pyplot as plt

class visualize:
    
    def __init__(self):
        pass
        
    def bargraph(self, dataSet):
        pass
    

    def piechart(self, dataSet):
        labels = []
        sizes = []
        total = 0
        for i in dataSet:
            labels.append(i[0])
            sizes.append(i[1])
            total += i[1]
        
        other = 0
        '''
        for i in range(len(sizes)):
            if i < len(sizes):
                if float(sizes[i])/total < 0.05:
                    del labels[i]
                    other += sizes[i]
                    del sizes[i]
                    i = i-1
        '''
        
        count = 0
        for i in sizes:
            if float(i)/total < 0.05:
                count += 1
                other += i
                
        if other > 0:
            sizes = sizes[:-count]
            labels = labels[:-count]
            labels.append("Other")
            sizes.append(other)
                
        
        def autopct_more_than_5(pct):
            return ('%1.f%%' % pct) if pct > 5 else ''
        '''
        def autolbl_more_than_5(pct):
            return labels[i] if pct > 5 else ''
        '''
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax1.set_title("Percentage of Trending Videos by Category")
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