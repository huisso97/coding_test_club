C = int(input())
for i in range(C):
    #0인덱스는 학생의 수 
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for score in scores[1:]:        
        if score > avg:
           cnt += 1
    result =  (cnt / scores[0]) * 100 
    print(round(result,3)+'%')
