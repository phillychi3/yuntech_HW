import random

rd = []
for i in range(100):
    rd.append(random.randint(0, 100))
print("max", max(rd))
print("low", min(rd))
print("all", sum(rd))
print("average", sum(rd) / len(rd))
print("0~30分的人數", len([i for i in rd if i <= 30]))
print("31~60分的人數", len([i for i in rd if 31 <= i <= 60]))
print("61~100分的人數", len([i for i in rd if 61 <= i <= 100]))
