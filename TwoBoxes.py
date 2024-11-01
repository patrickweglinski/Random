#TwoBoxes 10/30/24
#By Patrick, Skyler, Jace
from math import sqrt, exp, factorial, floor
import random as r
from random import random
import matplotlib.pyplot as plt

#total number of molecules
n = 1000
t = 10000

#molecules in box
nLeft = n/2

#lists for plotting
tList = [0]*t
nLeftList = [1]*t
hist = [0] * len(nLeftList)

for i in range(t):

    tList[i] = i 

    if (int(random()*n)) < nLeft:
        nLeft-=1
        # nLeftList[i] = nLeft

    else:
        nLeft+=1
        # nLeftList[i] = nLeft

    nLeftList[i] = nLeft

# plt.plot(tList, nLeftList, marker="o", markersize=3,color="blue", linestyle="None")
# plt.grid()
# plt.title("NLeft molecules over time")
# plt.xlabel("time")
# plt.ylabel("nleft amount")
# plt.show()

for i in range(len(nLeftList)):
    hist[i] = nLeftList[i]

plt.bar(nLeftList, hist)
plt.title("NLeft molecules over time")
plt.xlabel("time")
plt.ylabel("nleft amount")
plt.show()


    








