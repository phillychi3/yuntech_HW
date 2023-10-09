# 簡易排序

import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

ct = int(str[0])
thelist = []
for i in range(ct):
    thelist.append(int(str[i+1]))


thelist.sort()
for i in thelist:
    print(i)    