#RandomWalks 10/30/24
#By Patrick, Skyler, Jace
import random 
import math 
import matplotlib.pyplot as plt

walkers = 1
timesteps = 1000
position = 0
walkplot = [0]*timesteps
legend = []
distance = [0]*walkers

#variables for the rms calculation 
net = 0
rms = 0

walkplot[0] = position

while walkers < 20:

    #resetting position for new walker
    position = 0

    #simulating direction it walks away from the origin
    for i in range(timesteps-1):
        
        #walker moves in one direction or the other
        if random.random() < .5:
            position -= 1

        else:
            position += 1

        #recording every step taken for the display
        walkplot[i+1] = position

    #appending a new timestep to the timestep list
    legend.append(t)
        
    plt.plot(range(len(walkplot)),walkplot,marker="+", markersize=3)
    plt.grid() 
    plt.title("Random Walk")
    plt.xlabel("steps")
    plt.ylabel("distance away from origin")

    walkers +=1
    net += position**2

#calculating the root means squared to find typical expected net distance from the origin
rms = math.sqrt(net)/math.sqrt(t)
print(rms)

plt.show()









