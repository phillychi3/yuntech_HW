from random import randint

n = 3
cnt = 0
for i in range(n):
    rn1 = randint(1, 99)
    rn2 = randint(1, 99)

    def lol(cnt):
        try:
            ans = int(input(f"{rn1} X {rn2} = "))
            if ans == rn1 * rn2:
                cnt += 1
        except Exception as _:
            print("請輸入數字")
            lol(cnt)
        return cnt

    cnt = lol(cnt)

print(f"你答對{cnt}題，得分:{round(100*cnt/n,2)}")
