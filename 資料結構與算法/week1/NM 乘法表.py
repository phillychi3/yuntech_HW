import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]
data1 = str[0]
data2 = str[1]

for i in range(1, int(data1)+1):
    for j in range(1, int(data2)+1):
        print(str(i)+'*'+str(j)+'='+str(i*j))