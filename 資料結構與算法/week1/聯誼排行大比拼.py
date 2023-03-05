# 聯誼排行大比拼

import sys
str = sys.stdin.readlines()
str = [s.strip('\n') for s in str]
print(str)
# str = ['4', 'Nick 1', 'Peter 10', 'Bob 90', 'Alice 100']

ct = int(str[0])
data = {}
for i in range(ct):
    data[str[i+1].split(' ')[0]] = {
        'score': int(str[i+1].split(' ')[1]),
        'name': str[i+1].split(' ')[0]
    }

sorted_data = sorted(data.items(), key=lambda x: x[1]['score'], reverse=True)
print(sorted_data[0][1]['name'])
for i in range(ct):
    if sorted_data[i][1]['score'] == sorted_data[i+1][1]['score']:
        print(sorted_data[i+1][1]['name'])
    else:
        break


# import sys

# lines = sys.stdin.read().splitlines()

# lines.pop(0)  # 資料數 不重要 直接pop

# highest = 0
# fuck_boy = []
# for line in lines:
#     name, score = line.split()
#     score = int(score)
#     if score > highest:  # 更新標準
#         fuck_boy.clear()
#         highest = score
#     if score == highest:  # 加入渣男名單
#         fuck_boy.append(name)
# for i in fuck_boy:
#     print(i)