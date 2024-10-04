import jieba
import os

# 根據   Yuntech_QA.txt，建立字典

# 輸入: Yuntech_QA.txt
# 條件: 去停用字: [‘你(妳)’, ‘我’, ‘他(她)’, ‘她們’, ’他們’, ‘你們’, ‘我們’]及標點符號
# 輸出:
# (1) 使用Python字典語法生成“中文字典”及回傳“字典長度”
# (2) 假設: 我如何提報英檢成績?
# 輸出: (1)  token [‘如何’, ‘提報’, ‘英檢’, ‘成績’]
# (2) index ((word to index): [ 4, 5, 89, 43]

thispath = os.path.dirname(__file__)
with open(os.path.join(thispath, "Yuntech_QA.txt"), "r", encoding="utf8") as f:
    data = f.read()
out = {}

stopwords = {}.fromkeys(
    [
        line.rstrip()
        for line in open(os.path.join(thispath, "stopworld.txt"), encoding="utf8")
    ]
)

for line in data.split("\n"):
    for x in jieba.cut(line):
        if x not in stopwords:
            out[x] = len(out)


print(out)

tt = "我如何提報英檢成績"
ttd = []

for x in jieba.cut(tt):
    if x not in stopwords:
        ttd.append(x)
print(ttd)
print([out[x] for x in ttd])
