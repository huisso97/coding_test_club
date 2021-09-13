import sys
sys.stdin = open('1475.txt')

number = list(map(int, input().split()))
#방문표시 접근은 세트를 여러번 쓸 수 없다
#9를 없애서 카운트하는 식으로 접근해보자
#9가 들어오면 6에 플러스 1
num_list = [0,1,2,3,4,5,6,7,8,9]
#[0 0 0 3 0 0 2 0 0 ]
tmp = [False]*10
cnt = 1
for i in range(len(number)):
    if number[i] == 6 and tmp[6] == True and tmp[9] == False:
        tmp[9] = True
    elif number[i] == 9 and tmp[9] == True and tmp[6] == False:
        tmp[6] = True
    #숫자 1세트에 숫자가 있고, 사용하지 않았으면
    if number[i] in num_list and tmp[number[i]] == False:
        #True 바꾸기
        tmp[number[i]] = True
    else:
        tmp = [False]*10
        #세트 추가
        cnt += 1
print(cnt)
