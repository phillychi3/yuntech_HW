# 聯誼話題相親數
import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]


# def findallprime(n):
#     prime = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             prime.append(i)
#     return prime


# for i in str:
#     if i == '0':
#         break
#     else:
#         n = int(i)
#         prime = findallprime(n)
#         aall = sum(prime)
#         # find Amicable numbers
#         for j in range(1, 2000):
#             if j in prime:
#                 continue
#             else:
#                 jall = sum(findallprime(j))
#                 if jall in prime:
#                     continue
#                 else:
#                     if jall == aall:
#                         print(j)
#                         break
#                     else:
#                         continue
#         else:
#             print('QQ')
