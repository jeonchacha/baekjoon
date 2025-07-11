len = int(input())
data = []
for i in range(len):
    data.append(list(map(int,input().split())))
for i in data:
    sum = 0
    for j in i:
        sum += j
    print(sum)
           