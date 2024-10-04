# 聯誼訊系比大小

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]


# count = int(str[0])
# datas = []
# for i in range(count):
#     datas.append(str[i+1].split(' '))

# for i in range(count):
#     if int(datas[i][0]) == int(datas[i][1]):
#         print('DRAW')
#         continue
#     elif int(datas[i][2]) == 1:
#         if int(datas[i][0]) > int(datas[i][1]):
#             print('A')
#         else:
#             print('B')
#     else:
#         if int(datas[i][0]) < int(datas[i][1]):
#             print('A')
#         else:
#             print('B')
