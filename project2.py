import random
import matplotlib.pyplot as plt

n=1000
result = []
for i in range(n):
    circle_cnt = 0
    for j in range(i+1):
        x = random.random()
        y = random.random()
        if (x*x+y*y)**0.5 <= 1:
            circle_cnt +=1
    result.append(circle_cnt/(i+1)*4)

plt.plot(result)
plt.axhline(y=3.14, color="r", linewidth=1)
plt.show()