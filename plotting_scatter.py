import csv
import matplotlib.pyplot as plt
import numpy as np

with open("data/World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

header = data.pop(0)
print(header)

homicide_per_100k = []
firearms_per_100 = []
labels = []
for x in data: print(x[0], end=" ")

for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        # no poliitical unrest, long established, progressive, wealthy, no drug wars, no wars or border to war.
        if country[0] in ["Canada", "France", "Germany", "England and Wales", "Iceland", "South Korea", "Japan", "Australia", "Spain","Denmark", "Finland", "Sweden", "India", "Israel", "Switzerland", "Netherlands", "Austria", "Hungary", "United States"]:
            labels.append(country[0])
            homicide_per_100k.append(homicides)
            firearms_per_100.append(firearms)
    except:
        print(country[0], "did not print")

m, b = np.polyfit(firearms_per_100, homicide_per_100k, 1)
print(labels)
plt.figure(1, figsize=(12,7))
plt.scatter(firearms_per_100, homicide_per_100k)
plt.ylabel("homicides per 100k people")
plt.xlabel("guns per 100 people")

fit_x = [0, 100]
fit_y = [b, 100 * m]
plt.plot(fit_x, fit_y)

for i in range(len(labels)):
    if labels[i] != "":
        plt.annotate(
        labels[i], xy=(firearms_per_100[i], homicide_per_100k[i]), xytext=(5, 5), textcoords='offset points', ha='left', va='top', bbox=dict(boxstyle='round,pad=0.5', fc='lightblue', alpha=0.3), fontsize=8)

plt.show()
