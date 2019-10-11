from time import clock
import random

def riddle(A):
    if len(A) == 1:
        return A[0]

    else:
        temp = riddle(A[0:-1])

        if temp <= A[-1]:
            return temp
        else:
            return A[-1]


valid = True
for i in range(1, 999):
    rand_list = [random.randint(0, 99) for j in range(i)]

    start = clock()
    B = riddle(rand_list)
    print(i, "\t", clock() - start)
    C = min(rand_list)

    if B != C:
        valid = False

    if not valid:
        print("An error occurred")
        break

print("Success")



