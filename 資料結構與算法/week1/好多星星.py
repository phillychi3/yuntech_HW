import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]
data = int(str[0])

for i in range(data):
    print('*'*(i+1))