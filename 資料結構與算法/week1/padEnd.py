# padend

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]
strin = str[0]
llen = str[1]
pad = str[2]
wanttoadd = int(llen) - len(strin)
if wanttoadd > 0:
    flag = 0
    for i in range(wanttoadd):
        strin += pad[flag]
        flag += 1
        if flag == len(pad):
            flag = 0
print(strin)
