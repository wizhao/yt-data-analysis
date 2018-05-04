import analyze as az

usData = az.country('USvideos.csv')
caData = az.country('CAvideos.csv')
deData = az.country('DEvideos.csv')
frData = az.country('FRvideos.csv')
gbData = az.country('GBvideos.csv')

usSort = usData.channel_sort()
usChannel = usData.category_analysis()

deSort = deData.channel_sort()
deChannel = deData.category_analysis()

caSort = caData.channel_sort()
caChannel = caData.category_analysis()

frSort = frData.channel_sort()
frChannel = frData.category_analysis()

gbSort = gbData.channel_sort()
gbChannel = gbData.category_analysis()

usData.makePieChart()





print usChannel
print "\n"
print caChannel
print "\n"
print deChannel
print "\n"
print frChannel
print "\n"
print gbChannel