# 最大連續和

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

ct = int(str[0])
data = []
for i in range(ct):
    data.append(int(str[i + 1]))

max = 0
now = 0

for i in data:
    now += i
    if now > max:
        max = now
    if now < 0:
        now = 0
print(max)
