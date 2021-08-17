#문자열로 받는다
#빈 리스트 생성
#인덱스가 'O'이면 리스트 [i]에 +1 을 쌓는다
#인덱스가 아니면 0 
n = int(input())
for i in range(n):
    quiz = list(input())
    result = 0
    result_sum = 0
    for j in quiz:
        if j == 'O':
            result += 1
            result_sum += result
        else:
            result = 0 


