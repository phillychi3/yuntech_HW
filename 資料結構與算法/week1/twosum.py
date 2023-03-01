# twosum

import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]

setdata = str[0].split(" ")

target = int(setdata[1])

data = str[1].split(" ")
data = [int(i) for i in data]

uwu = {

}
for i in range(len(data)):
    if data[i] in uwu:
        print(uwu[data[i]], i)
        break
    else:
        uwu[target-data[i]] = i
