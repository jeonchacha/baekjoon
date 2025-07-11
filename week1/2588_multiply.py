# 예제 입력을 잘 볼것
# 123 456
# a,b=map(int,input().split())

# 123
# 456
a = int(input())
b = int(input())

result=[]
digits=[]

# 1의 자릿수부터 추출
while(b!=0):
    digits.append(b%10)
    b=b//10

# 각 자릿수와 곱한 값
for i in digits:
    result.append(a*i)

# 최종 계산
sum=0
temp=1
for i in result:
    sum += i*temp
    temp *=10 

result.append(sum)

for i in result:
    print(i)