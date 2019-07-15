from matplotlib import pyplot as plt
import random

# X axis range in the graph
age_x = [x for x in range(25,36)]


# Y axis values in the graph, len needs to be equal obvio
salaries_y = [random.randrange(65000,75000) for x in range(11)]
pysalaries_y = [random.randrange(70000,90000) for x in range(11)]

# plt func needs xval and yval for the most basic plotting, add label for
# extra functionalites such as using them as a differentiator for legends
plt.plot(age_x, salaries_y, label = 'regular salaries')
plt.plot(age_x, pysalaries_y, label = 'python salaries')

# adding more info to the graphs via title, x/y labelling
plt.title('salaries by age')
plt.xlabel('AGE')
plt.ylabel('SALARIES')

# to add a legend just to differentaite the lines
# first one is regular salaries from the list
# legend can accept lists of strings to be used
# can be empty if plots are labelled
plt.legend()

# To add another line to the plot we need to use another plt.plot()

plt.show()
