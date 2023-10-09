# import sys
# str = sys.stdin.readlines()
# str = [s.strip('\n') for s in str]
data = int(4)
# 聖誕樹
for i in range(data):
    print(' '*(data-i-1)+'*'*(i+1) + '*'*i)
# 樹根
for i in range(1,data):
    print(' '*(data-1)+"|")
