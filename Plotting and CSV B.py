import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr



with open("data/Libraries_-_2017_Computer_Sessions_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

names = [x[0] for x in data]  # grabbing list of library names (alphabetical)
names = names[1:]  # chop off header
print(names)

ytd = [x[-1] for x in data][1:]
ytd = [int(x) for x in ytd]
print(ytd)

library_number = [x for x in range(len(names))]
print(library_number)

# We want to plot computer users YTD vs library.

plt.figure(1, figsize=(12, 8), tight_layout=True, facecolor="lightblue")
plt.bar(library_number, ytd, color='red')
plt.title("Chicago Library Branch Computer Usage - 2017")
plt.ylabel("Computer Users")

plt.xticks(library_number, names, rotation=90, fontsize=8)  #  plotted data, text to plot

# Make a line graph of comp users at three libraries by month

print(data)
month_names = data.pop(0)[1:-1]
print(month_names)

#data = data[1:]

month_numbers = [x for x in range(12)]
print(month_numbers)

library_names = [x[0] for x in data]
print(library_names)

bwp_data = data[library_names.index('Bucktown-Wicker Park')][1:-1]
#bwp_data.pop(0)
#bwp_data.pop()
bwp_data = [float(x) for x in bwp_data]
print(bwp_data)

lp_data = data[library_names.index('Lincoln Park')][1:-1]
#bwp_data.pop(0)
#bwp_data.pop()
lp_data = [int(x) for x in lp_data]
print(lp_data)

hp_data = data[library_names.index('Humboldt Park')][1:-1]
#bwp_data.pop(0)
#bwp_data.pop()
hp_data = [int(x) for x in hp_data]
print(hp_data)

fig = plt.figure(2, tight_layout=True)
ax = fig.gca()

plt.plot(month_numbers, bwp_data, label="Bucktown Wicker Park")
plt.plot(month_numbers, hp_data, label="Humboldt Park")
plt.plot(month_numbers, lp_data, label="Lincoln Park")
plt.xticks(month_numbers, month_names, rotation=45)

#ax.get_yaxis().set_major_formatter(tkr.FuncFormatter(lambda x, p: format(int(x), '.2e')))

ax.yaxis.set_major_formatter(tkr.FuncFormatter(lambda p, x: format(int(x), '.2e')))

plt.legend(bbox_to_anchor=(0, 1), loc="upper left")

plt.show()