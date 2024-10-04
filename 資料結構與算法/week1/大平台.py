# 大平台
import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]
# str = "1 1 2 2 2 3 3 3 4 4"
data = str[1].split(" ")
data = [int(i) for i in data]

# 尋找出現次數最多的數字的次數
max = 0
for i in data:
    if data.count(i) > max:
        max = data.count(i)
print(max)
