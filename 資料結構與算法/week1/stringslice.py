# string slice

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

data = str[0]

flag1 = int(str[1])
flag2 = int(str[2])

print(data[flag1:flag2])
