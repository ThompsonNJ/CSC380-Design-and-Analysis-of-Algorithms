from time import process_time
from random import randint


## Part a
def euclid(m, n):
    while n != 0:
        temp = m % n
        m = n
        n = temp

    return m


# Part b
def consec_int(m, n):
    temp = min(m, n)
    while True:
        if m % temp == 0:
            if n % temp == 0:
                return temp

        temp -= 1


# Part a
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
gcd_eu = euclid(num_1, num_2)
print("The greatest common divisor of {} and {} using Euclid's algorithm is {}.".format(num_1, num_2, gcd_eu))

# Part b
gcd_ci = consec_int(num_1, num_2)
print("The greatest common divisor of {} and {} using Consecutive integer checking is {}.\n".format(num_1, num_2, gcd_ci))

# Part c
upper_limits = [i for i in range(6)]
lower_limits = [i for i in range(len(upper_limits))]

upper_limits[0] = randint(100, 999)
lower_limits[0] = randint(100, 999)

upper_limits[1] = randint(1000, 9999)
lower_limits[1] = randint(1000, 9999)

upper_limits[2] = randint(10000, 99999)
lower_limits[2] = randint(10000, 99999)

upper_limits[3] = randint(100000, 999999)
lower_limits[3] = randint(100000, 999999)

upper_limits[4] = randint(1000000, 9999999)
lower_limits[4] = randint(1000000, 9999999)

upper_limits[5] = randint(10000000, 99999999)
lower_limits[5] = randint(10000000, 99999999)

mean_eu = 0
mean_ci = 0

for i in range(len(upper_limits)):
    start_eu = process_time()
    gcd_eu = euclid(lower_limits[i], upper_limits[i])
    end_eu = process_time()
    total_eu = end_eu - start_eu
    mean_eu += total_eu

    start_ci = process_time()
    gcd_ci = consec_int(lower_limits[i], upper_limits[i])
    end_ci = process_time()
    total_ci = end_ci - start_ci
    mean_ci += total_ci

    print("The greatest common divisor of {} and {} using Euclid's algorithm is {}."
          .format(lower_limits[i], upper_limits[i], gcd_eu))
    print("The greatest common divisor of {} and {} using Consecutive integer checking is {}."
          .format(lower_limits[i], upper_limits[i], gcd_ci))

    print("\nTotal time taken for Euclid's algorithm: {}".format(total_eu))
    print("Total time taken for Consecutive integer checking is {}\n".format(total_ci))

print("Average time taken for Euclid's algorithm: {}".format(mean_eu / len(upper_limits)))
print("Average time taken for Consecutive integer checking: {}".format(mean_ci / len(upper_limits)))