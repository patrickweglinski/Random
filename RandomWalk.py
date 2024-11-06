#RandomWalks 10/30/24
#By Patrick, Skyler, Jace

import random 
import math 
import matplotlib.pyplot as plt

t = 1
timesteps = 1000
position = 0
walkplot = [0]*timesteps
legend = []
distance = [0]*t
net = 0
rms = 0

# while t <= 1:

walkplot[0] = position

while t < 20:

    position = 0

    for i in range(timesteps-1):
        
        if random.random() < .5:
            position -= 1

        else:
            position += 1

        walkplot[i+1] = position

    legend.append(t)
        
    plt.plot(range(len(walkplot)),walkplot,marker="+", markersize=3)
    plt.grid()
    plt.title("Random Walk")
    plt.xlabel("steps")
    plt.ylabel("distance away from origin")
    # plt.legend(legend)

    t +=1

    net += position**2

rms = math.sqrt(net)/t
print(rms)

plt.show()









