from collections import Counter 

a = int(input())
b = int(input())
c = int(input())

calc = a*b*c
num_list = list(map(int,str(calc)))

for i in range(10):
    count = 0
    for j in num_list:
        if i == j:
            count += 1
    print(count)

result = Counter(str(calc))
print(result)