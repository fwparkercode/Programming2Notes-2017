import matplotlib.pyplot as plt
import csv
import numpy as np

with open("data/World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

print(data)
headers = data.pop(0)
print(headers)

# Homicide by firearm rate per 100k vs Average firearms per 100

homicide_per100k = []
firearm_per100 = []
country_names = []

# no wars, no political unrest, established democracies or similar.
countries_to_plot = ["United States", "France", "Germany", "England and Wales", "Netherlands", "Sweden", "Norway", "Iceland", "Canada", "Japan", "South Korea", "China", "Australia", "Poland"]

for i in range(len(data)):
    if data[i][0] in countries_to_plot:
        try:
            homicide = float(data[i][5])
            firearm = float(data[i][7])
            name = data[i][0]
            country_names.append(name)
            homicide_per100k.append(homicide)
            firearm_per100.append(firearm)
        except:
            print("Failed", data[i][0])

plt.figure(1, figsize=(12, 7))
plt.scatter(firearm_per100, homicide_per100k)

print(country_names)
for i in range(len(country_names)):
    plt.annotate(country_names[i], xy=(firearm_per100[i], homicide_per100k[i]), xytext=(1, 1), textcoords='offset points')

m, b = np.polyfit(firearm_per100, homicide_per100k, 1)  # 1 for linear (returns m and b)
#plt.axis([0,100,0,3])
x = [0, 100]
y = [point * m + b for point in x]
plt.plot(x, y)

plt.title("World Firearm Deaths")
plt.ylabel("Homicides per 100k population")
plt.xlabel("Firearms per 100 population")

plt.show()

'''
labels[i], xy=(firearms_per_100[i], homicide_per_100k[i]), xytext=(5, 5), textcoords='offset points', ha='left', va='top', bbox=dict(boxstyle='round,pad=0.5', fc='lightblue', alpha=0.3), fontsize=8
'''