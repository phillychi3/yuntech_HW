list1to100 = list(range(1, 101))
non = []
# find all non-primes in list1to100
for i in list1to100:
    for j in range(2, i):
        if i % j == 0:
            non.append(i)
            break

print(non)
