import random
import matplotlib.pyplot as plt
import numpy as np

cnt = 0
max_size = 10000
x3 = []
y3 = []
x4 = []
y4 = []
for i in range(max_size):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)

    if y<= np.sin(np.pi *x):
        x3.append(x)
        y3.append(y)

for i in range(max_size):
    x = random.uniform(-1.0, 0)
    y = random.uniform(-1.0, 0)

    if y>= np.sin(np.pi *x):
        x4.append(x)
        y4.append(y)


print(cnt/max_size * 1)

plt.scatter(x3, y3, c='black')
plt.scatter(x4, y4, c='blue')

plt.show()