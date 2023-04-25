# 判斷質數
import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

ct = int(str[0])

for i in range(1, ct+1):
    n = int(str[i])
    if n == 1:
        print('Composite')
    else:
        for j in range(2, n):
            if n % j == 0:
                print('Composite')
                break
        else:
            print('Prime')