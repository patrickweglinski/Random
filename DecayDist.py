#DecayDist 10/30/24
#By Patrick, Skyler, Jace

import random 
import math 
import matplotlib.pyplot as plt

#amount of nuclei
n = 1000
timesteps = 100
decayList = []
decayed = 0

for i in range(timesteps):

    decayed = 0

    for i in range(n):

        if int(random.random()*1000) == 1:

            decayed += 1

        decayList.append(decayed)

plt.bar(range(len(decayList)),decayList)
plt.grid()
plt.title("Nuclear Decay Per Timestep")
plt.xlabel("Timestep")
plt.ylabel("amount of non-decayed nuclei per timestep")
plt.show()
    
