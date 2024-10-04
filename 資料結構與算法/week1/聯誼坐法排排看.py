import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]

# count = int(str[0])

# if count == 4:
#     a = [1, 2]
#     b = [3, 4]
# elif count == 8:
#     a = [1, 2, 3, 4]
#     b = [5, 6, 7, 8]
# elif count == 16:
#     a = [1, 3, 5, 7, 9, 11, 13, 15]
#     b = [2, 4, 6, 8, 10, 12, 14, 16]

# for i in range(int(str[1])):
#     x = int(str[i+2])
#     if x in a:
#         a[a.index(x)] = 'x'
#     elif x in b:
#         b[b.index(x)] = 'x'

# outdata = []

# for i in range(len(a)):
#     if i < len(a)-1:
#         if a[i] is not 'x' and a[i+1] is not 'x':
#             outdata.append((a[i], a[i+1]))
# for i in range(len(b)):
#     if i < len(b)-1:
#         if b[i] is not 'x' and b[i+1] is not 'x':
#             outdata.append((b[i], b[i+1]))
# for i in range(len(a)):
#     if i < len(b):

#         if a[i] is not 'x' and b[i] is not 'x':
#             outdata.append((a[i], b[i]))

# outdata = list(set(outdata))
# print(len(outdata))
