import random

def rpm(n, m):
    product = 0
    num_additions = 0
    num_mult_and_div = 0
    while n > 0:
        if n % 2 == 1:
            product += m
            num_additions += 1

        n >>= 1
        m <<= 1
        num_mult_and_div +=1

    return num_additions, num_mult_and_div


for i in range(100000, 100000000, 100000):
    n = random.randint(99000, i)
    m = random.randint(99000, i)
    num_additions, num_mult_and_div = rpm(n,m)
    print(i, "\t", num_additions, "\t", num_mult_and_div)