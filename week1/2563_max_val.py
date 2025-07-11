data = []
for i in range(9):
    num = int(input())
    data.append(num)

max_val = data[0]
max_idx = 1

# slice: list[start:end]
# end - 1 번째 까지
for i in data[1:]:
    if max_val < i:
        max_val = i
        max_idx = data.index(i) + 1

print(max_val)
print(max_idx)

