# 貪婪的小偷
# import sys
# str = sys.stdin.readlines()
# str = [s.strip('\n') for s in str]

# # str = [3,5,1,3,5,7,9]
# max價值 = int(str[0])
# 物品數量 = int(str[1])

# 物品 = []
# for i in range(2, len(str)):
#     物品.append(str[i])

# 物品 = list(map(int, 物品))
# 物品.sort(reverse=True)
# 總價值 = 0
# for i in range(max價值):
#     總價值 += 物品[i]
# print(總價值)

import sys

lines = sys.stdin.read().splitlines()
c = int(lines.pop(0))
lines.pop(0)
items = list(map(int, lines))
items.sort(reverse=True)
print(sum(items[:c]))