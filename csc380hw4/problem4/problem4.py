import random

def lomuto_partition(A, left, right):
    count = 0
    p = A[left]
    s = left
    for i in range(left+1, right+1):
        count += 1
        if A[i] < p:
            s += 1
            temp = A[s]
            A[s] = A[i]
            A[i] = temp

    temp = A[s]
    A[s] = A[left]
    A[left] = temp

    print(len(A), "\t", count)
    return s


def quick_select(A, left, right, k):
    s = lomuto_partition(A, left, right)
    if s == k - 1:
        return A[s]
    elif s > left + k - 1:
        return quick_select(A, left, s - 1, k)

    else:
        return quick_select(A, s + left, right, k - 1 - s)


my_list = [random.randint(1, 1000000000) for i in range(1000000)]
qs = quick_select(my_list, 0, len(my_list) - 1, 1)