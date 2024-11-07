#Decay 10/30/24
#By Patrick, Skyler, Jace

import random 
import math 
import matplotlib.pyplot as plt

#amount of nuclei
n = 10000
time = 0
nList = [1]*n
time = []
stop = n*.1
decayed = 0

while n != stop:

    decayed = 0

    for i in range(n):

        if int(random.random()*1000) == 1:

            decayed += 1
            nList[i] = 1
            
    n -= decayed
        



plt.plot(range(len(nList)),nList,marker="+", markersize=3)
# plt.xlim(0,10E6)
# plt.ylim(0,10E6) 
plt.grid()
plt.title("Nuclear Decay")
plt.xlabel("time")
plt.ylabel("amount of non-decayed nuclei")
plt.show()
    
