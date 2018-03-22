import csv
import matplotlib.pyplot as plt

with open("data/Libraries_-_2017_Computer_Sessions_by_Location.csv") as f:
    reader = csv.reader(f) # make a reader object
    data = list(reader)  # casting the reader object as a list

names = [x[0].strip() for x in data][1:]  # all chi library names (alphabetical)
name_index = [x for x in range(len(names))]
#print(name_index)

ytd = [x[-1] for x in data][1:]
ytd = [int(x) for x in ytd]  #  year to date computer sessions for libraries
#print(ytd)

# grab data for three libraries


# plot ytd vs library as a bar graph

plt.figure(1, figsize=(12, 6), tight_layout=True, facecolor="lightblue")
plt.bar(name_index, ytd, color="red", label="test2")
plt.xticks(name_index, names, rotation=90, fontsize=8)  # indexed list, strings list
plt.title("Chicago Library Computer Sessions - 2017", fontsize=25)
plt.ylabel("Computer Users")

#plt.show()


# plot three libraries

headers = data.pop(0)
print(headers)
print(names)

print(names.index("Lincoln Park"))  # index of Lincoln Park
print(names.index("Lincoln Belmont"))
print(names.index("Sulzer Regional"))

month_names = headers[1:-1]
print(month_names)

month_numbers = [x for x in range(12)]

sulzer_y = data[names.index("Sulzer Regional")][1:-1]
sulzer_y = [int(x) for x in sulzer_y]
lb_y = data[names.index("Lincoln Belmont")][1:-1]
lb_y = [int(x) for x in lb_y]
lp_y = data[names.index("Lincoln Park")][1:-1]
lp_y = [int(x) for x in lp_y]

plt.figure(2, tight_layout=True)
plt.plot(month_numbers, sulzer_y, label="Sulzer")
plt.plot(month_numbers, lb_y, label="Lincoln and Belmont")
plt.plot(month_numbers, lp_y, label="Lincoln Park")

plt.ylabel("Computer Users")
plt.title("Computer Users per Month (2017)")
plt.xticks(month_numbers, month_names, rotation=45)
plt.legend(bbox_to_anchor=(0.75,0.4), loc="center")

plt.show()