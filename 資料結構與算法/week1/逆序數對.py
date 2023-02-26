# 逆序數對

import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

str = str[1].split(' ')
thelist = [int(i) for i in str]


# count = 0
# copy = []

# for i in thelist:
#     copy.append(i)
# copy.sort()

# for i in range(len(copy)):
#     count += thelist.index(copy[i])
#     thelist.remove(copy[i])
# print(count)