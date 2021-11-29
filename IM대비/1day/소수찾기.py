n = int(input())
numbers = map(int,input().split())
#맵함수로 정수로 전환된 값들을 저장
cnt = 0
for num in numbers:
    notsosu = 0
    if num > 1: 
        for i in range(2, num):
            if num % i == 0 :
               notsosu +=1 
        if notsosu == 0 :
            cnt += 1
print(cnt)

# Thank you