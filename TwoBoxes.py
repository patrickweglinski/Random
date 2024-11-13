#TwoBoxes 10/30/24
#By Patrick, Skyler, Jace
#Simulation using random functions of collection of 
#gas molecules moving between two boxes

from math import sqrt, exp, factorial, floor
import random as r
from random import random
import matplotlib.pyplot as plt

#total number of molecules
n = 100

#number of timesteps
t = 100000

#molecules in box
nLeft = n//2

#lists for plotting
tList = [0]*t
nLeftList = [1]*t
hist = [0] * (n + 1)


#main loop that will adjust the numbers of molecules in each box
for i in range(t):

    tList[i] = i 

    #if the randomly generated number is less than the amount of molecules in
    #the left box decrement the amount of molecules in the left box. Increment the 
    #molecules in the left box otherwise. 
    if (int(random()*n)) < nLeft:
        nLeft-=1

    else:
        nLeft+=1

    nLeftList[i] = nLeft

    hist[int(nLeft)] += 1


# plt.plot(tList, nLeftList, marker="o", markersize=3,color="blue", linestyle="None")
# plt.grid()
# plt.title("NLeft molecules over time")
# plt.xlabel("time")
# plt.ylabel("nleft amount")
# plt.show()

#these are our plotting ranges
min = 0
max = 0

#using for loops to find where the bounds of the graph should be
for i in range(len(hist)):
    
    if hist[i] > 0:
        min = i-1
        break

for i in range(len(hist)):
    
    if hist[i] > 0:
        max = i+1

# plt.bar(range(len(hist)),hist)
# plt.title("Number of events Nleft value occured")
# plt.xlim(min,max)
# plt.xlabel("value")
# plt.ylabel("events")
# plt.show()

#manual function that outputs the probability given a binomial distribution range
def probability(n,nLeft): 
    return(1/2**n)*(factorial(n))/(factorial(nLeft)*(factorial(n-nLeft)))

#creating the lists for the our new plot, filling, and initializing them
probabilityList = [0]*n

leftbucket = 0

for i in range(n):
    probabilityList[i] = t*probability(n, leftbucket)
    leftbucket+=1

#histogram plotted with the binomial distribution function output as a line imposed on the
#histogram.
plt.plot(range(len(probabilityList)),probabilityList,linestyle="solid", color="red")
plt.bar(range(len(hist)),hist,label="Monte Carlo results")
plt.title("Probabilty of events and number of events")
plt.xlabel("value")
plt.ylabel("events and probability of the event")
plt.legend(["probability","events"])
plt.show()








