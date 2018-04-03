import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open("311_Service_Requests_-_Alley_Lights_Out.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data.pop(0)
print(headers)

print(data[:10])

print(len(data))
completed = [x for x in data if x[1] == 'Completed']
print(len(completed))
date_format = "%m/%d/%Y"

time_data = []

for i in range(len(completed)):
    try:
        d1 = datetime.strptime(completed[i][2], date_format)
        d2 = datetime.strptime(completed[i][0], date_format)
        delta = abs((d2 - d1).days)
        time_data.append(completed[i] + [delta])
    except:
        #print("Nope")
        pass


# we are now working with time_data set, normal set plus call time at [-1]
zips_counted = []
#_time_data = time_data[:]
zip_data = []

for i in range(len(time_data)):
    zip = time_data[i][6]

    if zip not in zips_counted:
        zips_counted.append(zip)
        calls = []
        for j in range(len(time_data)):
            if time_data[j][6] == zip:
                calls.append(time_data[j][-1])

        #print(time_data[i][6], len(calls), sum(calls)/len(calls))
        zip_data.append([time_data[i][6], len(calls), sum(calls)/len(calls)])

print(zip_data.sort(key=lambda x: x[2]))

for zip in zip_data: print(zip)



zip_codes = [x[0] for x in zip_data][2:]
avg_days = [x[2] for x in zip_data][2:]
avg_days = [int(x) for x in avg_days]

zip_dummy = [x for x in range(len(zip_codes))]

plt.figure(1, tight_layout=True)
plt.bar(zip_dummy, avg_days)
plt.xticks(zip_dummy, zip_codes, rotation=90)
plt.show()

