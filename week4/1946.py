# 1946 신입사원
import sys
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    grade = [tuple(map(int, input().split())) for _ in range(N)]

    def recruit(grade):
        grade.sort()
        minimum_score = grade[0][1]
        count = 1
        for i in grade[1:]:
            if minimum_score < i[1]: continue
            count += 1
            minimum_score = i[1]

        return count

    print(recruit(grade))