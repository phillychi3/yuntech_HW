# 比大小

import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

for i in str:
    a, b = i.split(' ')
    a = int(a)
    b = int(b)
    if a == b == 0:
        continue
    elif a > b:
        print(a)
    else:
        print(b)