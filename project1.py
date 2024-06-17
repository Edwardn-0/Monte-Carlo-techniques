import matplotlib.pyplot as plt
import random

n=1000
x_list = []
y_list = []
circle_x = []
circle_y = []
for i in range(n):
    x = random.random()
    y = random.random()
    if (x*x+y*y)**0.5 <= 1:
        circle_x.append(x)
        circle_y.append(y)
    else:
        x_list.append(x)
        y_list.append(y)

print(len(circle_x) / n*4)
    
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(5,5))
plt.title("원주율: " +str(len(circle_x)/n*4))
plt.scatter(x_list, y_list)
plt.scatter(circle_x, circle_y, c="r")

plt.show()