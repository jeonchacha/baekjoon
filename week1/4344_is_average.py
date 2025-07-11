# student_count = int(input())
# while True:
#     try:
#         student_score = list(map(int, input(f"{student_count} 명의 점수를 입력하세요: ").split()))
#         if len(student_score) != student_count:
#             raise ValueError(f"{student_count} 명의 점수를 입력해야 합니다.")
#     except ValueError as e:
#         print(e)
#         continue
#     else:
#         break
 
student_group = int(input())
student_score = []
for i in range(student_group):
    data = list(map(int,input().split()))
    student_score.append(data)

for i in student_score:
    student_count = i[0]
    
    sum = 0
    average = 0.0
    good_job = 0
    for j in i[1:]:
        sum += j
        average = sum / student_count
 
    for j in i[1:]:
        if j > average:
            good_job += 1

    result = round(good_job / student_count * 100, 3)
    print(f"{result}%")