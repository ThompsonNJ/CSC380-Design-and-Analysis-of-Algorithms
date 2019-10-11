import random

def insertion_sort(A):
    count = 0
    for i in range(1, len(A)):
        v = A[i]
        j = i - 1
        
        while j >= 0 and A[j] > v:
            count += 1
            A[j+1] = A[j]
            j -= 1
            
        A[j+1] = v

    return count

for n in range(100, 3000, 100):
    my_list = [random.randint(1, n) for i in range(n)]
    my_list_is = insertion_sort(my_list)
    print(n, "\t", my_list_is)

    # if my_list_is != sorted(my_list):
    #     print("Something went wrong!")

