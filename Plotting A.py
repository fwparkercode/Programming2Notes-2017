#  PLOTTING
# matplotlib is the plotting library for python

import matplotlib.pyplot as plt

plt.figure(1)
plt.plot([1, 2, 3, 4, 10])  # when no x is specified, just assigns according to index
plt.plot([10, 4, 3, 2, 1])  # plots to same graph

plt.figure(2)  # opens up a new window
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  #  can specify x and y "lists"

# customizing your graph/plot using kwargs
plt.plot([1, 2, 3, 4], [1, 2, 3, 4], c='green', linestyle=':', marker='^', markersize=10, alpha=0.5)
'''
c or color = color as a string
ls or linestyle = '-' solid, '--' dashed, '-.' dot dash, ':' dotted
marker = '.', '+', ^, o
markersize = float (pixels)
alpha = transparency from 0 to 1
'''

plt.axis([0, 10, 0, 10])  # xmin, xmax, ymin, ymax
plt.ylabel('my data (units)')
plt.xlabel('my scale (units)')
plt.title('Hello World', color="blue", fontsize=30)


plt.show()
