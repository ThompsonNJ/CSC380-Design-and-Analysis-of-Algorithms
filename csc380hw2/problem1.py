from time import clock

S = 0
# n = 1000000000000
# n = 10000000000000000
n = 1000000000000000000000

for i in range(1, n + 1, 1000000000000000000):
    start = clock()
    S += i * i
    print(str(i) + "\t" + str(clock() - start))

# Part e
# No need to time this as it is obviously O(1)
# A = n * (n+1) * (2*n+1) // 6
# print(A)

