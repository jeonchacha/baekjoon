# 1931 회의실 배정
import sys
input = sys.stdin.readline

N = int(input().strip())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

def schedule_meetings(meetings):
    meetings.sort(key=lambda x:(x[1], x[0]))
    end_time = 0
    count = 0
    for start, end in meetings:
        if start >= end_time:
            end_time = end
            count += 1
    return count

result = schedule_meetings(meetings)
print(result)