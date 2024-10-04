"""
題目：
一個背包限重至多為W與放入N個物品。其中每個物品皆有重量與價值。每一個物品你可以選擇放入背包或不放入背包使得背包在限重範圍內達到最大價值。請問背包可達到的最大價值是多少?。

輸入測資說明： 測試資料會有數組，每組的第一行有兩個整數N(1<=N<=1000), W(1<=W<=1000)分別代表物品數量和背包限重。 接著有 N 行，每一行皆有2個正整數分別代表物品重量和價值，用空白隔開。(範圍為1~1000)

此題請使用Decision Tree(決策樹)解題
測試輸入資料請複製以下內容，貼上至網頁右上角"T"按鈕的黃色便條中，再按執行。
4 13
3 5
1 2
2 1
1 4
3 20
2 10
11 31
9 2

預期結果應為
12
41
"""


def maxvalue(n, w, weight, value):
    """
    n: 物品數量
    w: 背包限重
    weight: 物品重量
    value: 物品價值
    """
    if n == 0 or w == 0:
        return 0
    if weight[n - 1] > w:
        return maxvalue(n - 1, w, weight, value)
    else:
        return max(
            maxvalue(n - 1, w, weight, value),
            maxvalue(n - 1, w - weight[n - 1], weight, value) + value[n - 1],
        )


while 1:
    try:
        n, w = map(int, input().split())
        weight = []
        value = []
        for i in range(n):
            ww, v = map(int, input().split())
            weight.append(ww)
            value.append(v)
        print(n, w, weight, value)
        print(maxvalue(n, w, weight, value))
    except:
        break
