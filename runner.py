import analyze as az

usData = az.country('USvideos.csv')
caData = az.country('CAvideos.csv')
deData = az.country('DEvideos.csv')
frData = az.country('FRvideos.csv')
gbData = az.country('GBvideos.csv')

usSort = usData.channel_sort()
usChannel = usData.category_analysis()
usOther = usData.likes_dislikes_comments()

deSort = deData.channel_sort()
deChannel = deData.category_analysis()
deOther = deData.likes_dislikes_comments()

caSort = caData.channel_sort()
caChannel = caData.category_analysis()
caOther = caData.likes_dislikes_comments()

frSort = frData.channel_sort()
frChannel = frData.category_analysis()
frOther = frData.likes_dislikes_comments()

gbSort = gbData.channel_sort()
gbChannel = gbData.category_analysis()
gbOther = gbData.likes_dislikes_comments()

#usData.makePieChart()
#usData.makeBarGraph()
fullData = [usData.ScatterPlotData(), caData.ScatterPlotData(), 
            deData.ScatterPlotData(), frData.ScatterPlotData(),
            gbData.ScatterPlotData()]

usData.makeScatterPlot(fullData)

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