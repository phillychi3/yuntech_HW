import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]


target = str[0]
ct = int(str[1])
data = []
for i in range(2, ct + 2):
    if str[i] != target:
        data.append(str[i])

for i in data:
    print(i)
