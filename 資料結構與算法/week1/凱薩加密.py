import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]


位移 = str[0]
data = str[1]

for i in data:
    if i.isalpha():
        if i.isupper():
            print(chr((ord(i) - ord('A') + int(位移)) % 26 + ord('A')), end='')
        else:
            print(chr((ord(i) - ord('a') + int(位移)) % 26 + ord('a')), end='')
    else:
        print(i, end='')