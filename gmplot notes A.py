from gmplot import *
import csv
import random

apikey = "AIzaSyBS-5jK3PZ1RtojwY_QBCl-kAVY1-v6sDQ"

mymap = GoogleMapPlotter(41.923127, -87.638219, 10, apikey=apikey)  # lat, long, zoom_level, apikey=var

mymap.marker(41.923127, -87.638219)  # lat, long

mymap.circle(41.933127, -87.638219, 500, "#FF0000", ew=3)  # lat, long, radius(m), web_color, edge_width=int

my_lats = [41.923127 + x/50 for x in range(10)]
my_longs = [-87.638219 + x/50 for x in range(10)]

mymap.plot(my_lats, my_longs, "blue")

my_lats = [41.923127, 41.933127, 41.923127]
my_longs = [-87.638219, -87.648219, -87.658219]
mymap.polygon(my_lats, my_longs, fc="yellow", ew=10, ec="red") # lats, longs, color, facecolor, edgewidth, edgecolor


with open("data/Parks_-_Public_Art.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
size = [random.randrange(1,500) for x in data]

mymap.scatter(lats, longs, marker=False, color="red", size=10, alpha=0.5)

#for i in range(len(lats)):
#    mymap.circle(lats[i], longs[i], size[i])

mymap.heatmap(lats, longs, maxIntensity=2, radius=50, dissipating=True)


mymap.draw('mymap.html')
