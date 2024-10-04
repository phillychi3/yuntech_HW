# 聯誼門票搶起來


import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

n = int(str[0])
adr = ""
for i in range(n):
    adr += str[i + 1]
m = int(str[n + 1])
output = ""
for i in range(m):
    output += adr[int(str[n + 2 + i]) - 1]
print(output)
