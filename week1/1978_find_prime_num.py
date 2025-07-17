import math

N = int(input())
num = map(int,input().split())
prime_num_count = 0
for i in num:
    is_prime = True
    # 1은 소수에서 제외
    if i < 2:
        continue
    # O(N) -> 제곱근(root) 으로 개선
    # 곱으로 나타낼 수 있는 경우를 절반까지만 확인하면 됨 -> 그 뒤로는 조합의 역방향일뿐
    # +1 은 range의 동작방식이 end 미만 이기 때문
    for j in range(2,int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:    
        prime_num_count += 1
print(prime_num_count)
