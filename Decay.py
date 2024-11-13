#Decay 10/30/24
#By Patrick, Skyler, Jace
import random 
import math 
import matplotlib.pyplot as plt

#amount of nuclei
n = 10000
t = 0
nList = []
stop = n*.1
decayed = 0

#stop is set to .1 x n. So once 90 percent of the molecules decays, stop.
while n != stop:

    decayed = 0

    for i in range(n):

        #this means that if the number generated is 1 specific number out of 1000, the particle decays
        #or, .001 chance to decay. 
        if int(random.random()*1000) == 1:

            decayed += 1

    t+=1 
    #removing the amount decayed from the total molecules
    n -= decayed
    nList.append(n)

plt.plot(range(t),nList,marker="+", markersize=3)
plt.grid()
plt.title("Nuclear Decay")
plt.xlabel("time")
plt.ylabel("amount of non-decayed nuclei")
plt.show()
    
