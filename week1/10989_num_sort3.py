import sys
# 벤치마크 결과 sys.stdin.readline()이 input()보다 약 10배 빠름
# input(): 내부적으로 sys.stdin.readline() 호출한 뒤 끝에 붙은 \n 제거, 이 제거 작업은 C 레벨에서 수행되어 비교적 빠름
# sys.stdin.readline().strip() 은 앞뒤 공백 모두 제거
# strip()는 파이썬 레벨에서 수행돼 가장 느림, 개행문자만 제거할거면 rstrip() 사용

# int() 함수는 문자열 양쪽 공백(whitespace)을 자동으로 무시하고 숫자를 파싱 -> 불필요하게 strip() X
n = int(sys.stdin.readline())

# counting sort
# 등장횟수 저장
count = [0] * 10001
# 입력받은 숫자의 등장 횟수만 카운팅 (정렬 불필요) -> 인덱스 자체가 값
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

# 등장했다면 등장 횟수만큼 출력 
for i in range(1, 10001):
    # if 0: false, 그외의 값 true
    if count[i]:
        # 출력도 병목이 될 수 있으므로 많은 출력을 처리할 땐 sys.stdout.write()를 사용 -> 메모리초과
        # sys.stdout.write((str(i)+'\n') * count[i])
        for _ in range(count[i]):
            print(i)