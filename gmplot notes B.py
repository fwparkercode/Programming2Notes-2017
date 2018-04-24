from gmplot import *
import csv

apikey = "AIzaSyAg79NYNeuKv5_du1jUhnd-867W76HOOAI"

mymap = GoogleMapPlotter(41.923412, -87.638176, 12, apikey=apikey)

mymap.marker(41.923412, -87.638176)  # lat, long

mymap.circle(41.933412, -87.638176, 500, "#FF0000", ew=10)  # lat, long, radius(m), color, ew=

lats = [41.923412 for x in range(10)]
longs = [-87.638176 - x/100 for x in range(10)]
lats[4] = 41.933412

mymap.plot(lats, longs, "blue", ew=10)  # lats, longs, color

mymap.polygon(lats, longs, fc="red", ec="black") # lats, longs, color, facecolor(fc), edgecolor(ec)

with open("data/Parks_-_Public_Art.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))

lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]

mymap.scatter(lats, longs, marker=True)

'''
for i in range(len(lats)):
    mymap.circle(lats[i], longs[i], i, "green")  # like scatter, but we can vary color and size
'''

mymap.heatmap(lats, longs, maxIntensity=10, radius=50, dissipating=True)

mymap.draw("mymap.html")

