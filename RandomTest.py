#RandomTest 10/30/24
#By Patrick, Skyler, Jace
#Visualizing the spread of randomly generated numbers
from math import sqrt, exp, factorial, floor
import random as r
from random import random
import matplotlib.pyplot as plt

 
#Outputting lists of randomly generated numbers

# for i in range(20):
#     print(random())

# for i in range(20):
#     print(random())

# for i in range(50):
#     print(int(10*random()))


#displaying 1000 randomly generated coordinates on a grid.
#lists that hold the coordinates for the grid

x = [0]*1000
y = [0]*1000

for i in range(1000):
    x[i] = 10*random()

for i in range(1000):
    y[i] = 10*random()

plt.plot(x, y,marker="+", markersize=3,color="blue", linestyle="None")
plt.axis("scaled")
plt.xlim(0,10)
plt.ylim(0,10)
plt.xticks(range(11))
plt.yticks(range(11))
plt.grid()
plt.title("1000 random points")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
    








