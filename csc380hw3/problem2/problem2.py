def brute_force_string_match(T, P):
    count = 0
    for i in range(len(T) - len(P) + 1):
        count += 1
        j = 0
        while j < len(P) and P[j] == T[i + j]:
            count += 1
            j += 1

        if j == len(P):
            print(count)
            return i

    print(count)
    return -1

test = ""
for i in range(1000):
    test += "0"

a = "00001"
b = "10000"
c = "01010"


brute_force_string_match(test, a)
brute_force_string_match(test, b)
brute_force_string_match(test, c)
brute_force_string_match(test, d)


