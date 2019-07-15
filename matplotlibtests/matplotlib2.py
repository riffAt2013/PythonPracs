from matplotlib import pyplot as plt
import random

# to get a different falvor of plotting we can use different style files
# to get a list of availvale style use 
# print(plt.style.available)
plt.style.use('bmh')
# plt.xkcd() for xkcd style plots 

# X axis range in the graph
age_x = [x for x in range(25,36)]

# in case you dont understand this tells us that
# the line is going to markered with a dot at the points of 
# data, it'll be green and solid
# types of marker style, o = for circle
# . for dotted, ^ for triangle
pythonformat_str = '.g-'

# Y axis values in the graph, len needs to be equal obvio
salaries_y = [random.randrange(65000,75000) for x in range(11)]
pysalaries_y = [random.randrange(70000,90000) for x in range(11)]
jssalaries_y = [random.randrange(60000,80000) for x in range(11)]


# coming from the last tut, we used format strings of following format
# '[color][linestyle]', 'b--' tells us that the line is blue and dashed
# to know anout fomrat strings in matplotlib readthedocs
plt.plot(age_x, salaries_y, 'b--o', label = 'regular salaries')
plt.plot(age_x, pysalaries_y, pythonformat_str, label = 'python salaries')


# well we can create owr own formatted string style via kwargs, again we can pass 
# hex color values to color kwarg, not be used in a typical formatted string
# the linewidth kwarg is used for bolder lines, defval is 1
plt.plot(age_x, jssalaries_y, color = "#444444", marker = '^', linewidth = 1, label = 'Javascript salaries')
plt.legend()
plt.title('salaries by age')
plt.xlabel('AGE')
plt.ylabel('SALARIES')


# for gridding the plot to get better perspectives
# plt.grid(True)
# plt.tight_layout() for padding issues in a laptop
plt.show()