import math
import time
import random

def BFCP_sqrt(P):
    d = math.inf
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            d = min(d, ((P[i][0] - P[j][0])**2) + (P[i][1] - P[j][1])**2) ** 0.5

    return d

def BFCP_revised(P):
    d = math.inf
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            d = min(d, ((P[i][0] - P[j][0]) ** 2) + ((P[i][1] - P[j][1]) ** 2))

    return d ** 0.5
                    
for n in range(0, 3001, 250):
    my_points = []
    for i in range(n):
        my_points.append((random.randint(1000000000000, 10000000000000), random.randint(1000000000000, 10000000000000)))

    start_sqrt = time.clock()
    dist_CP_sqrt = BFCP_sqrt(my_points)
    end_sqrt = time.clock()

    start_revised = time.clock()
    dist_CP_revised = BFCP_revised(my_points)
    end_revised = time.clock()

    print(n, "\t", end_sqrt - start_sqrt, "\t", end_revised - start_revised)