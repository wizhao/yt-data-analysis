import analyze as az

usData = az.country('USvideos.csv')

usSort = usData.channel_sort()
print usSort