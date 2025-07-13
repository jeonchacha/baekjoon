import sys

height_list = [int(sys.stdin.readline()) for _ in range(9)]

height_list.sort()
total = sum(height_list)
fake_i = fake_j = 0
# 총합에서 두명 제거
for i in range(len(height_list)-1):
    for j in range(i+1, len(height_list)):
        if height_list[i] + height_list[j] == total - 100:
            fake_i, fake_j = i, j

for idx, height in enumerate(height_list):
    if idx == fake_i or idx == fake_j:
        continue
    print(height)