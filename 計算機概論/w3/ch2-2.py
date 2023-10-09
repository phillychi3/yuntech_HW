data = []
for i in range(3):
    data.append(input("input three number"))
data2 = [int(i) for i in data if int(i) % 2 != 0]
try:
    print(max(data2))
except:
    print(min(data))

