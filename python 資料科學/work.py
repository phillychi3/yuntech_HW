import pandas as pd


data1 = ["紅茶", "綠茶", "奶茶", "冰淇淋紅茶", "蛋糕紅茶","蛋塔紅茶"]
data2 = ["紅色的茶", "綠色的茶", "大兵奶茶", "冰淇淋紅茶", "蛋糕紅茶","蛋塔紅茶"]
data3 = ["茶", "這是茶", "大奶茶", "冰淇淋紅茶", "蛋糕大紅茶","蛋塔紅茶"]

df1 = pd.DataFrame(data1, columns=["品項"])
df2 = pd.DataFrame(data2, columns=["品項"])
df3 = pd.DataFrame(data3, columns=["品項"])
df = pd.merge(df1, df2, on="品項", how="inner")
df = pd.merge(df, df3, on="品項", how="inner")
print(df)