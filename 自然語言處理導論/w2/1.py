import jieba
import os
import jieba.posseg as psg

thispath = os.path.dirname(__file__)
jieba.load_userdict(os.path.join(thispath, "dict.txt"))
with open(os.path.join(thispath, "file.txt"), "r", encoding="utf8") as f:
    data = f.read()
out = []

for x in psg.cut(data):
    if x.flag == "nr":
        out.append(x.word)
out = list(set(out))
print(out)
print(str(len(out)) + "個人名")
