import matplotlib.pyplot as plt

x_val = [1,2,3,4,5,6,7,8,9,10]
y_val = [1,4,6,8,10,12,14,16,18,20]

# this is how to do a simple line graph

# plt.plot(x_val, y_val, color = 'green')
# plt.xlabel("x-axis placeholder")
# plt.ylabel("y-axis placeholder")
# plt.title("Title placeholder")
# plt.show()

# this is how to do a scatter plot. Just put scatter

# plt.scatter(x_val, y_val, color = 'green')
# plt.xlabel("x-axis placeholder")
# plt.ylabel("y-axis placeholder")
# plt.title("Title placeholder")
# plt.show()

# barchart
# name = ['cat', 'dog', 'horse', 'fish']
# name_value = [10, 30, 100, 1]
# plt.bar(name, name_value, color = 'forestgreen') # use chat gpt to search for the colors to use
# plt.xlabel("Animals")
# plt.ylabel("Weight")
# plt.title("Weight per animal")
# plt.show()


# histogram
import numpy as np
x_normal = np.random.normal(0, 1, 100000)
# plt.hist(x_normal, color = 'forestgreen')
# plt.xlabel('X')
# plt.ylabel("Frequency")
# plt.title("randomly sampled data")
# plt.show()

# population distribution
from scipy.stats import norm
x_vals = np.arange(-4,4,0.01)
y_vals = norm.pdf(x_vals)
counts, bins, ignored = plt.hist(x_normal, 30, density=True, color="forestgreen", label='sampling distribution')
plt.plot(x_val, y_val, color = 'y', linewidth=2.5, label='population distribution')
plt.xlabel('X')
plt.ylabel("Frequency")
plt.title("randomly generating 1000")
plt.legend()
plt.show()

# The population distribution doesn't quite work, I don't know why. My question is...
# Why isn't the yellow line going exactly around the green bar chart?