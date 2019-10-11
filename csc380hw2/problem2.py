from time import clock

# A = [[0, 0], [0, 0]]
# A = [[1, 1], [0, 0]]
A = [[0 for i in range(1000)] for i in range(1000)]

flag = True
for i in range(0, len(A) - 1):
    #start = clock()
    for j in range(1, len(A)):
        if A[i][j] != A[j][i]:
            flag = False
            break
    #print(clock() - start)

print(flag)