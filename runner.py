import analyze as az
from visualize import *

usData = az.country('USvideos.csv')
caData = az.country('CAvideos.csv')
deData = az.country('DEvideos.csv')
frData = az.country('FRvideos.csv')
gbData = az.country('GBvideos.csv')

usSort = usData.channel_sort()
usChannel = usData.category_analysis()
usOther = usData.likes_dislikes()

deSort = deData.channel_sort()
deChannel = deData.category_analysis()
deOther = deData.likes_dislikes()


caSort = caData.channel_sort()
caChannel = caData.category_analysis()
caOther = caData.likes_dislikes()


frSort = frData.channel_sort()
frChannel = frData.category_analysis()
frOther = frData.likes_dislikes()


gbSort = gbData.channel_sort()
gbChannel = gbData.category_analysis()
gbOther = gbData.likes_dislikes()

barData = [usData.barGraphData(), caData.barGraphData(),
           deData.barGraphData(), frData.barGraphData(),
           gbData.barGraphData()]
           
scatterData = [usData.scatterPlotData(), caData.scatterPlotData(), 
            deData.scatterPlotData(), frData.scatterPlotData(),
            gbData.scatterPlotData()]

scatter = visualize()
scatter.scatterplot(scatterData)                       


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