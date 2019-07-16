from matplotlib import pyplot as plt
import random
import numpy as np

# to get a different falvor of plotting we can use different style files
# to get a list of availvale style use 
# print(plt.style.available)

# plt.xkcd() 

# X axis range in the graph
age_x = [x for x in range(25,36)]
# this naive method didnt work surprisingly
# x_indexes = [x for x in range(len(age_x))]
x_indexes = np.arange(len(age_x))

width_value = 0.25


salaries_y = [random.randrange(65000,75000) for x in range(11)]
pysalaries_y = [random.randrange(70000,90000) for x in range(11)]
jssalaries_y = [random.randrange(60000,80000) for x in range(11)]


# plotting multiple bars create issues such as overlapping of the bars
# so that some of the datas are completely submerged inside one 
# we can fix this via offsetting
plt.bar(x_indexes - width_value, salaries_y, width = width_value, color = "#FBE864", label = 'regular salaries')
plt.bar(x_indexes, pysalaries_y, width = width_value,  label = 'python salaries')
plt.bar(x_indexes + width_value, jssalaries_y, width = width_value,  label = 'Javascript salaries')

plt.legend()

# strangely cant put kwargs in it, but it shouldve been
# ticks = x_indexes, labels = age_x
# the usage of this func is still unknown
plt.xticks(x_indexes, age_x)

plt.title('salaries by age')
plt.xlabel('AGE')
plt.ylabel('SALARIES')


# plt.grid(True)

plt.show()