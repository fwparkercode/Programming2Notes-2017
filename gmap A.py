from gmplot import *

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"
mymap = GoogleMapPlotter(41.8781, -87.6298, 10, apikey=apikey)


mymap.marker(37.427, -122.145)  # lat long
mymap.marker(37.428, -122.146)
mymap.marker(37.429, -122.144)

mymap.circle(37.429, -122.145, 100, "#FF0000", ew=2)  # lat long size, color, linewidth



path = [(37.428, 37.427, 37.427),
         ( -122.145, -122.145, -122.146)]
path2 = [[i+.01 for i in path[0]], [i+.02 for i in path[1]]]
path3 = [(37.433302 , 37.431257 , 37.427644 , 37.430303), (-122.14488, -122.133121, -122.137799, -122.148743)]
path4 = [(37.423074, 37.422700, 37.422410, 37.422188, 37.422274, 37.422495, 37.422962, 37.423552, 37.424387, 37.425920, 37.425937),
     (-122.150288, -122.149794, -122.148936, -122.148142, -122.146747, -122.14561, -122.144773, -122.143936, -122.142992, -122.147863, -122.145953)]


mymap.plot(path[0], path[1], "white", edge_width=10, edge_color="red")  # draws a path (lats, longs, html_color)

mymap.polygon(path3[0], path3[1], edge_color="cyan", edge_width=5, face_color="blue", face_alpha=0.1)  # (lats, longs, kwargs (color, edge_width, edge_color, edge_alpha, face_alpha, face_color)

#mymap.heatmap(path4[0], path4[1], threshold=10, radius=40)
mymap.heatmap(path4[0], path4[1], maxIntensity=2, radius=100, dissipating=True)


# marker or circle to mark position
mymap.scatter(path4[0], path4[1], color='black', marker=True)
#mymap.scatter(path4[0], path4[1], s=90, marker=False, alpha=0.1)


mymap.draw('./mymap.html')