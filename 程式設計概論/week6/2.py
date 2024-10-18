import requests
import nltk
from nltk import word_tokenize
from collections import defaultdict

nltk.download("punkt")
nltk.download("stopwords")

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = requests.get(url)
response.encoding = "utf-8-sig"

tokens = word_tokenize(response.text)
tokens2 = [e.lower() for e in tokens if e.lower() >= "a" and e.lower() <= "z"]


mydict = defaultdict(list)
for t in tokens2:
    mydict[t[0]].append(t)

for key in sorted(mydict.keys()):
    words_list = mydict[key]
    print(f"{key} => {len(words_list)} => {words_list[:10]}")

mydict2 = {}
for t in tokens2:
    mydict2[t] = mydict2.get(t, 0) + 1

# for k,v in mydict2.items():
#     print(f"{k:20} => {v}")

n = 0
for k, v in sorted(mydict2.items(), key=lambda x: (-x[1])):
    if n == 20:
        break
    print(f"{k:20} => {v}")
    n += 1
