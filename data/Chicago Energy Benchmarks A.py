import matplotlib.pyplot as plt
import csv
import numpy as np
import random
import urllib.request


#url = "https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD"
#page = urllib.request.urlopen(url)
#print(page)

with open("Chicago_Energy_Benchmarking_-_2014_Data_Reported_in_2015.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)

ghg = []
sf = []
built_in = []
names = []
for i in range(len(data)):
    try:
        built = int(data[i][headers.index("Year Built")])
        electrical = int(data[i][headers.index("Total GHG Emissions (Metric Tons CO2e)")])
        square_ft = int(data[i][headers.index("Gross Floor Area - Buildings (sq ft)")])
        name = data[i][2]
        built_in.append(built)
        ghg.append(electrical)
        sf.append(square_ft)
        names.append(name)

    except:
        print("Value error")
        pass
print(ghg)
print(sf)

marker = [x/10000 for x in sf]

color_list = []
for built in built_in:
    if built < 1910:
        color_list.append("red")
    elif built < 1960:
        color_list.append("orange")
    elif built < 1980:
        color_list.append("yellow")
    elif built < 2010:
        color_list.append("green")
    else:
        color_list.append("blue")

m, b = np.polyfit(sf, ghg, 1)
'''
labels=[]
for i in range(len(ghg)):
    if ghg[i] / sf[i] > 0.055 or ghg[i]/sf[i] < 0.0065 or ghg[i] > 30000:
        labels.append(names[i])
    else:
        labels.append("")
'''
plt.figure(1, tight_layout=True, figsize=(12,7))
plt.plot([0, 10000000], [b, m * 10000000 + b])
plt.scatter(sf, ghg, color=color_list, alpha=0.5, s=50)
for i in range(len(names)):
    if names[i] != "":


        if ghg[i] / sf[i] > 0.055:
            plt.annotate(
                names[i], xy=(sf[i], ghg[i]), xytext=(0, max(40,i)),
                textcoords='offset points', ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc='red', alpha=0.3),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

        elif ghg[i]/sf[i] < 0.0065:  # 0.0065
            plt.annotate(
                names[i], xy=(sf[i], ghg[i]), xytext=(int(i), 0),
                textcoords='offset points', ha='left', va='top',
                bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.3),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
        elif ghg[i] > 40000:
            plt.annotate(
                names[i], xy=(sf[i], ghg[i]), xytext=(-40, 10),
                textcoords='offset points', ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.3),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

        else:
            pass



plt.xlabel("Square Feet")
plt.ylabel("Greenhouse Gas Emissions (Metric Tons C02)")
plt.title("Chicago Building Emissions (2015-2016)", fontsize=25)

plt.axis([0, 5e6, 0, 80000])
plt.show()

