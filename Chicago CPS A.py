import matplotlib.pyplot as plt
import csv
import numpy as np



with open("data/Chicago_Public_Schools_-_School_Progress_Reports_SY1516.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data[0])
print(data[0].index("One_Year_Dropout_Rate_Year_1_Pct"))

attend_pct = []
college_pct = []

data = data[1:]

for school in data:
    try:
        college = float(school[119])
        attend = float(school[114])
        if attend < 40:
            print(school[2])
        college_pct.append(college)
        attend_pct.append(attend)

    except:
        #print(school[2], "does not have data")
        continue

m, b = np.polyfit(attend_pct, college_pct, deg=1)



plt.figure(1)


plt.plot([0, 100], [b, b + m * 100], color='red')
plt.axis([0, 100, 0, 100])

plt.scatter(attend_pct, college_pct)
plt.show()


