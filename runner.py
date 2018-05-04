import analyze as az

usData = az.country('USvideos.csv')

usSort = usData.channel_sort()
#usChannel = usData.category_analysis()
print usSort