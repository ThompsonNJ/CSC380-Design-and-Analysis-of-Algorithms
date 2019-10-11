from time import process_time

with open('sieve_test.csv', 'w') as file:
    n = 100
    ## I recommended making the while loop smaller if you just want to verify the algorithm works.
    while n <= 500100:
        start = process_time()
        A = [i for i in range(n + 1)]
        A[0] = 0
        A[1] = 0

        for p in range(int(n ** (1/2))):
            if A[p] != 0:
                j = p * p
                while j <= n:
                    A[j] = 0
                    j += p

        L = []
        for p in range(2, n + 1):
            if A[p] != 0:
                L.append(A[p])

        ## Uncomment the line below to verify if the algorithm works.
        ## print("The list of prime numbers from 2 to {} is:\n{}".format(n, L))
        end = process_time()
        print("Time taken to calculate primes from 2 to {} is {}".format(n, end - start))
        file.write(str(end - start) + '\n')
        n += 100