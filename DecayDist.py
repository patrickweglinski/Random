#DecayDist 10/30/24
#By Patrick, Skyler, Jace

import random 
import math 
import matplotlib.pyplot as plt

#amount of nuclei
n = 10000
trials = 10000
decayList = [0]*n
poissonList = []
decayed = 0
probability = .001

print("runnning")

#function to calculate Poisson Distribution
def poisson(k, el):
    return((1/math.factorial(k))*(el**k)*(math.exp(-el)))

for i in range(trials):

    decayed = 0

    for i in range(n):

        if random.random() < probability:

            decayed += 1

    decayList[decayed] +=1

for i in range(int(10*probability*n)):

    poissonList.append(trials*poisson(i, (probability*n)))




plt.bar(range(len(decayList)),decayList)
plt.plot(range(len(poissonList)),poissonList,linestyle="solid", color="red")
plt.xlim(0,int(3*probability*n))
plt.grid()
plt.title("Nuclear decays of first trial")
plt.xlabel("Observed nuclear decays")
plt.ylabel("Number of events")
plt.legend(["histogram","poisson"])
plt.show()

# Jace was here