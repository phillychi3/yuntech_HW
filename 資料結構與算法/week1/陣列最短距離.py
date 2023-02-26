# 陣列最短距離

import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

x = [int(i) for i in str[1].split(' ')]
y = [int(i) for i in str[2].split(' ')]

min = 9999999999
xi = 0
yi = 0

while xi < len(x) and yi < len(y):
    if abs(x[xi] - y[yi]) < min:
        min = abs(x[xi] - y[yi])
    if x[xi] > y[yi]:
        yi += 1
    else:
        xi += 1

print(min)