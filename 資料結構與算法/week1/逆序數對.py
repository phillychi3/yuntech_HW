# 逆序數對

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

# str = str[1].split(' ')
# thelist = [int(i) for i in str]


# count = 0
# copy = []

# for i in thelist:
#     copy.append(i)
# copy.sort()

# for i in range(len(copy)):
#     count += thelist.index(copy[i])
#     thelist.remove(copy[i])
# print(count)


# import sys
# str = sys.stdin.readlines()
# str = [s.strip('\n') for s in str]

# str = str[1].split(' ')
# 數列 = [int(i) for i in str]

# 逆序數對總數 = 0

# def 分兩邊排序(數列):
#     if len(數列) == 1:
#         return 數列
#     else:
#         mid = len(數列)//2
#         left = 分兩邊排序(數列[:mid])
#         right = 分兩邊排序(數列[mid:])
#         return 合併(left, right)

# def 合併(left, right):
#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#             逆序數對總數 += len(left) - i
#     result += left[i:]
#     result += right[j:]
#     return result


# 分兩邊排序(數列)
# print(逆序數對總數)
