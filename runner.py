import analyze as az
from visualize import *

usData = az.country('USvideos.csv')
caData = az.country('CAvideos.csv')
deData = az.country('DEvideos.csv')
frData = az.country('FRvideos.csv')
gbData = az.country('GBvideos.csv')


usSort = usData.channel_sort()
deSort = deData.channel_sort()
caSort = caData.channel_sort()
frSort = frData.channel_sort()
gbSort = gbData.channel_sort()

barData = [usData.barGraphData(), caData.barGraphData(),
           deData.barGraphData(), frData.barGraphData(),
           gbData.barGraphData()]


usOther = usData.likes_dislikes()
deOther = deData.likes_dislikes()
caOther = caData.likes_dislikes()
frOther = frData.likes_dislikes()
gbOther = gbData.likes_dislikes()
           
scatterData = [usData.scatterPlotData(), caData.scatterPlotData(), 
            deData.scatterPlotData(), frData.scatterPlotData(),
            gbData.scatterPlotData()]


pieData = [usData.category_analysis(), deData.category_analysis(),
           caData.category_analysis(), frData.category_analysis(),
           gbData.category_analysis()]
           
scatter = visualize()
scatter.scatterplot(scatterData)

pie = visualize()
pie.piechart(usChannel)                                              


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