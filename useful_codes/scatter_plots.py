import matplotlib.pyplot as plt

# simple scatter
fig = plt.figure()

ax = fig.add_subplot(1,1,1)

ax.scatter(x1,y1)

ax.set_title('second scatter plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.show()

# print with some color label
sc = plt.scatter(X[:, 0], X[:, 1], vmin=-1, vmax=1, c=color_label)
plt.show()