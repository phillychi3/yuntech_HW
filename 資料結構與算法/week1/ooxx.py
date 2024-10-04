# ooxx

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]
# 判斷勝利
map = [
    list(str[0]),
    list(str[1]),
    list(str[2]),
]


# 判斷橫向
for i in range(2):
    if map[i][0] == map[i][1] == map[i][2]:
        print(map[i][0])
        sys.exit()

# 判斷直向
for i in range(2):
    if map[0][i] == map[1][i] == map[2][i]:
        print(map[0][i])
        sys.exit()
# 判斷斜向
if map[0][0] == map[1][1] == map[2][2]:
    print(map[0][0])
    sys.exit()
if map[0][2] == map[1][1] == map[2][0]:
    print(map[0][2])
    sys.exit()

# 判斷平手

print("DRAW")
