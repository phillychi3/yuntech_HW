# string endswith

import sys

str = sys.stdin.readlines()
str = [s.strip("\n") for s in str]
strin = str[0]
target = str[1]

if strin.endswith(target):
    print("true")
else:
    print("false")
