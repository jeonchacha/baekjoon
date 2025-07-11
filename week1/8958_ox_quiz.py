len = int(input())
quiz_list = []
for i in range(len):
    quiz = input()
    quiz_list.append(quiz)

# X면 연속점수 초기화
for i in quiz_list:
    # list 의 생성자에 문자열을 넣으면 char 로 구분된 배열을 반환
    ox_list = list(i)

    continuous_score = 0
    result = 0

    current = ox_list[0]
    if current == 'O':
        continuous_score = 1
        result = 1

    for i in ox_list[1:]:
        current = i
        continuous_score += 1

        if current == 'X':
            continuous_score = 0
        
        result += continuous_score

    print(result)

