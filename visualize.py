import matplotlib.pyplot as plt

class visualize:
    
    def __init__(self):
        pass
        
    def bargraph(self, dataSet):
        pass
    

    def piechart(self, dataSet):
        def autopct_more_than_5(pct):
            return ('%1.f%%' % pct) if pct > 5 else ''
            
        def makelists(data):
            self.total = 0
            labels = []
            sizes = []
            total = 0
            for j in data:
                labels.append(j[0])
                sizes.append(j[1])
                self.total += j[1]
            return sizes,labels
        
        def makeOther(sizes,labels):
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
        while i < len(dataSet):
            a,b = makelists(dataSet[i])
            sizes, labels = makeOther(a,b)
            if i == 0:
                plt.subplot(231)
                plt.pie(sizes, labels=labels, autopct=autopct_more_than_5, startangle=45,labeldistance=1.1)
                plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title("United States")
                
            elif i == 1:
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
        plt.title('Countries\' Trending Videos by Category')
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