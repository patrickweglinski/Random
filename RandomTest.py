#Random Processes 10/30/24
#By Patrick, Skyler, Jace
from math import sqrt, exp, factorial, floor
import random as r
from random import random
import matplotlib.pyplot as plt

# for i in range(20):
#     print(random())

# for i in range(20):
#     print(random())

# for i in range(50):
#     print(int(10*random()))

x = []
y = []

for i in range(1000):
    x[i] = 10*random()

for i in range(1000):
    y[i] = 10*random()

plt.plot(x, y,marker="o", markersize=2,color="red")
plt.show()
    








