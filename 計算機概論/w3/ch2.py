data = input("plz input ten numbers: ").split()
if len(data) == 1:
    for i in range(9):
        data.append(input("number"))
data = [int(i) for i in data if int(i) % 2 != 0]
if len(data) == 0: print("a message") 
else: print(max(data))


