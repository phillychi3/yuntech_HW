import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]
print(int(eval(str[0])))
