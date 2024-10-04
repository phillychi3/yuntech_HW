ll = [75, 74, 79, 76, 75, 76, 78, 77, 72, 73, 74, 79, 77, 74, 75]
ll.sort(reverse=True)
ld = 1
lct = 1
print("分數\t排名")
for ct,data  in enumerate(ll,1):
    if ld == data:
        print(f"{lct}\t{data}")
    else:
        ld = data
        lct = ct
        print(f"{ct}\t{data}")
