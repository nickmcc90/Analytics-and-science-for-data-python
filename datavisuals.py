import matplotlib.pyplot as plt

x_val = [1,2,3,4,5,6,7,8,9,10]
y_val = [1,4,6,8,10,12,14,16,18,20]

# this is how to do a simple line graph

plt.plot(x_val, y_val, color = 'green')
plt.xlabel("x-axis placeholder")
plt.ylabel("y-axis placeholder")
plt.title("Title placeholder")
# plt.show()

# this is how to do a scatter plot. Just put scatter

plt.scatter(x_val, y_val, color = 'green')
plt.xlabel("x-axis placeholder")
plt.ylabel("y-axis placeholder")
plt.title("Title placeholder")
plt.show()