import random
import time

def selection_sort(A):
    for i in range(len(A)-1):
        small = i
        for j in range(i + 1, len(A)):
            if A[j] < A[small]:
                small = j

        temp = A[i]
        A[i] = A[small]
        A[small] = temp

    return A

def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j+i] < A[j]:
                temp = A[j+i]
                A[j+i] = A[j]
                A[j] = temp
    return A


for n in range(100, 3001, 25):
    random_list = [random.randint(0,n) for i in range(n)]

    ss_start = time.clock()
    ss = selection_sort(random_list)
    ss_total = time.clock() - ss_start

    bs_start = time.clock()
    bs = bubble_sort(random_list)
    bs_total = time.clock() - bs_start

    if ss != bs:
        print("Something went wrong!")
        break

    print(str(n) +" \t" + str(ss_total) + "\t" + str(bs_total))
