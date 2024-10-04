# 搜尋數字


import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

第一行 = str[0].split(" ")
元素量 = int(第一行[0])
搜尋數字 = int(第一行[1])

list = []
for i in range(元素量):
    list.append(int(str[i + 1]))

list.sort()


# 不要問我為啥要用這個 腦中就浮現這算法
def binary_search(list, 目標):
    low = 0
    high = len(list) - 1
    while low <= high:
        中間 = (low + high) // 2
        猜 = list[中間]
        if 猜 == 目標:
            return 中間
        if 猜 > 目標:
            high = 中間 - 1
        else:
            low = 中間 + 1
    return -1


for j in range(搜尋數字):
    print(binary_search(list, int(str[元素量 + 1 + j])))
