a,b=input().split()

# ::(이중콜론) 은 슬라이싱에서 사용되는 문법
# sequence[start:stop:step]
# start stop 생략하고 step 만 지정

c,d = a[::-1], b[::-1]
print(c if c > d else d)

# 시퀀스 자료형: 순서가 존재하고 슬라이싱과 인덱싱이 가능한 객채
# list, tuple, str, range