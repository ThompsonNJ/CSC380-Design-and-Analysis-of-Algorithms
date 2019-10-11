import time

def Q(n):
    if n == 1:
        return 1
    
    return Q(n-1) + 2*n - 1

n = 100
start = time.clock()
A = Q(n)
print(time.clock() - start)
