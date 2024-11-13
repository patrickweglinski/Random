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

# print("what")

while n != stop:

    decayed = 0

    for i in range(n):

        if int(random.random()*1000) == 1:

            decayed += 1
    
    if t == 0:
        print(decayed)

    t+=1 
    n -= decayed
    nList.append(n)

plt.plot(range(t),nList,marker="+", markersize=3)
plt.grid()
plt.title("Nuclear Decay")
plt.xlabel("time")
plt.ylabel("amount of non-decayed nuclei")
plt.show()
    
