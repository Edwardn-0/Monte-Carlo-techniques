import random
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return np.sin(np.pi*x)

x_min = 0
x_max = 4
y_min = -1
y_max = 1

x_list = []
y_list = []
color_list = []
N = 10000

cnt = 0

for i in range(N):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)

    x_list.append(x)
    y_list.append(y)
    y_max = func(x)

    if y<=func(x):
        cnt+=1
        color_list.append('dodgerblue')
    else:
        color_list.append('red')



px = np.linspace(x_min, x_max, 1000)
py = func(px)

print(cnt/N * 4)
plt.plot(px, py, color='black')
plt.scatter(x_list, y_list, color = color_list, s=1)
plt.grid()
plt.show()