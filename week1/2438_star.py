floor = int(input())

for i in range(floor):
    # range(0) 은 작동안함
    for j in range(i+1):
        print('*', end = '')
    print()