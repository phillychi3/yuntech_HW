import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

# str = .#####
# .#####
# .#####
# .#####
# ......

# str = ['6 5',  '.#####', '.#####', '.#####', '.#####', '......']


setting = str[0].split(" ")

megon = []
for i in range(int(setting[1])):
    megon.append(list(str[i + 1]))

# # 走迷宮 只有一條路 道路是'.' 障礙物是'#'

# # 起點
# start = (0,0)
# # 終點
# end = (int(setting[0])-1, int(setting[1])-1)

# # 走過的路
# walked = []
# # 走路的步數
# steps = 0

# # 走迷宮
# def walk_megon(x, y):
#     global steps
#     global walked
#     global megon
#     global end
#     # 如果走到終點
#     if (x, y) == end:
#         return True
#     # 如果走到道路
#     if megon[x][y] == '.':
#         # 記錄走過的路
#         walked.append((x, y))
#         # 走路的步數 + 1
#         steps += 1
#         # 如果走到終點
#         if walk_megon(x+1, y):
#             return True
#         if walk_megon(x-1, y):
#             return True
#         if walk_megon(x, y+1):
#             return True
#         if walk_megon(x, y-1):
#             return True
#         # 如果走不到終點
#         # 走路的步數 - 1
#         steps -= 1
#         # 回到上一步
#         walked.pop()
#         # 標記為走過
#         megon[x][y] = '#'
#         return False

# walk_megon(0, 0)
# print(steps)


megon = []
for i in range(int(setting[1])):
    megon.append(list(str[i + 1]))

all = 0
for i in range(int(setting[1])):
    for o in range(int(setting[0])):
        if megon[i][o] == ".":
            if i + 1 < int(setting[1]) and megon[i + 1][o] == ".":
                all += 1
            elif i - 1 >= 0 and megon[i - 1][o] == ".":
                all += 1
            elif o + 1 < int(setting[0]) and megon[i][o + 1] == ".":
                all += 1
            elif o - 1 >= 0 and megon[i][o - 1] == ".":
                all += 1
print(all - 1)
