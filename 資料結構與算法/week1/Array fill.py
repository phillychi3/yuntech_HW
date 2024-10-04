import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]


target = str[0]
ct = int(str[1])
for _ in range(ct):
    print(target)
