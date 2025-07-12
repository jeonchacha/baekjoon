# 골드바흐의 추측: 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다
# 4=2+2, 6=3+3, 8=3+5, 10=5+5, 12=5+7

num_list = []
case = int(input())
for i in range(case):
    num_list.append(int(input()))

import math

def is_prime(num: int) -> bool:
    sqrt = int(math.sqrt(num))
    for i in range(2, sqrt+1):
        if num % i == 0:
            return False
    return True

# 소수 판별 리스트 만들기
def eratosthenes(max: int = 10000) -> list:
    # max + 1 : 리스트의 인덱스를 숫자 값 그대로 사용하기 위함
    prime_list = [True] * (max + 1)
    prime_list[0] = prime_list[1] = False
    
    sqrt = int(math.sqrt(max))

    for i in range(2, sqrt+1):
        # 리스트의 내용이 True인 2의 배수 False
        if prime_list[i]:
            # 2*2 부터 2step 씩
            for j in range(i*i, max + 1, i):
                prime_list[j] = False

    # 소수의 인덱스만 출력
    # for index, is_prime in enumerate(prime_list):
    #     if is_prime:
    #         print(index)    
    return prime_list

prime_list = eratosthenes()
    
for i in num_list:
    even_num = i
    # 2로 나눈 몫 까지만 반복, 그 뒤로는 조합의 역방향 
    mid_val = even_num // 2
    # 소수여야해서 2부터 시작
    a = 2
    b = even_num - a
    min = b
    min_a = 0
    min_b = 0
    while(a <= mid_val):
        # if is_prime(a) and is_prime(b):
        if prime_list[a] and prime_list[b]:
            # 골드바흐 파티션이 여러 가지의 경우 두 소수의 차이가 가장 작은 것을 출력
            if min > b - a:
                min = b - a
                min_a = a
                min_b = b
        a += 1
        b -= 1
    print(min_a, min_b)
    # 시간 초과 남 -> 에라토스테네스의 체: 특정 범위 내의 소수를 판별하는데 효과적

