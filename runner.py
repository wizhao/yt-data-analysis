import analyze as az
from visualize import *

usData = az.country('USvideos.csv') #gather data from csv files
caData = az.country('CAvideos.csv')
deData = az.country('DEvideos.csv')
frData = az.country('FRvideos.csv')
gbData = az.country('GBvideos.csv')


usSort = usData.channel_sort() #sorts data for further processing
deSort = deData.channel_sort()
caSort = caData.channel_sort()
frSort = frData.channel_sort()
gbSort = gbData.channel_sort()

barData = [usData.barGraphData(), caData.barGraphData(),
           gbData.barGraphData()] #truncates and sorts data for use in bar graph


usOther = usData.likes_dislikes() #adds up likes and dislikes for further processing
deOther = deData.likes_dislikes()
caOther = caData.likes_dislikes()
frOther = frData.likes_dislikes()
gbOther = gbData.likes_dislikes()
           
scatterData = [usData.scatterPlotData(), caData.scatterPlotData(), 
            deData.scatterPlotData(), frData.scatterPlotData(),
            gbData.scatterPlotData()] #organizes data for scatter plots


pieData = [usData.category_analysis(), deData.category_analysis(),
           caData.category_analysis(), frData.category_analysis(),
           gbData.category_analysis()] #analyzes data for use in pie chart

bar = visualize() #creates bar graphs
bar.bargraph(barData)

pie = visualize()  #creates pie charts
pie.piechart(pieData)
                   
scatter = visualize() #creates scatter plots
scatter.scatterplot(scatterData)                                          


#testing purposes
'''
print usChannel
print "\n"
print caChannel
print "\n"
print deChannel
print "\n"
print frChannel
print "\n"
print gbChannel
'''
