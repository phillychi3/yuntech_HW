# 走迷宮
# 自帶混淆:P lol
import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

迷宮大小 = str[0].split(' ')
迷宮大小 = [int(i) for i in 迷宮大小]

迷宮 = []
for i in range(迷宮大小[0]):
    迷宮.append(list(str[i+1]))


起點 = (0,0)
終點 = (迷宮大小[0]-1, 迷宮大小[1]-1)

列表 = []
走過的路 = []
紀錄 = {} 


列表.append(起點)
走過的路.append(起點)
紀錄[起點] = None

while 列表:
    current = 列表.pop(0)
    if current == 終點:
        break
    x = current[0]
    y = current[1]
    if x+1 < 迷宮大小[0] and 迷宮[x+1][y] == '.' and (x+1, y) not in 走過的路:
        列表.append((x+1, y))
        走過的路.append((x+1, y))
        紀錄[(x+1, y)] = current
    if x-1 >= 0 and 迷宮[x-1][y] == '.' and (x-1, y) not in 走過的路:
        列表.append((x-1, y))
        走過的路.append((x-1, y))
        紀錄[(x-1, y)] = current
    if y+1 < 迷宮大小[1] and 迷宮[x][y+1] == '.' and (x, y+1) not in 走過的路:
        列表.append((x, y+1))
        走過的路.append((x, y+1))
        紀錄[(x, y+1)] = current
    if y-1 >= 0 and 迷宮[x][y-1] == '.' and (x, y-1) not in 走過的路:
        列表.append((x, y-1))
        走過的路.append((x, y-1))
        紀錄[(x, y-1)] = current

current = 終點
走路 = 0
while current != 起點:
    current = 紀錄[current]
    走路 += 1

print(走路)
