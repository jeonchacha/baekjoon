t= int(input())
str_list = []
for i in range(t):
    s = input().split()
    str_list.append(s)
for i in range(t):
    concat = ''
    count = int(str_list[i][0])

    separate = list(str_list[i][1])
    for j in separate:
        for k in range(count):
            concat += j
    print(concat)
