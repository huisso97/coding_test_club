import sys
sys.stdin = open('6190.txt')


#곱한 값이 단조증가수인지 확인해서 맞으면, 모아서 그 중 곱의 최댓값 구하기
#없으면 -1

# T = int(input())
# 
# 
# for tc in range(1, T+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     tmp = []
#     for i in range(0, len(arr)-1):
#         #j의 범위는 i의 바로 다음이 아니고 i보다 큰 모든 수라서 따로 범위 지정
#         for j in range(i+1, n):
#             #런타임에러라서 바로 str로 바꿔줌
#             num = str(arr[i] * arr[j])
#             if len(str(num)) == 1:
#                 tmp.append(int(num))
#             else:
#                 cnt = 0
#                 for k in range(0, len(num)-1):
#                     if int(num[k]) <= int(num[k+1]):
#                         cnt += 1
#                     else:
#                         break
#                 if cnt == len(num)-1:
#                     tmp.append(int(num))
#     if not tmp:
#         print('#{} -1'.format(tc))
#     else:
#         print('#{} {}'.format(tc, max(tmp)))
# 
# 






# if result:
#     print('#{} {}'.format(tc, result))








'''
나랑 다음값을 곱할거야 
걔를 나눈 몫과 나머지를 비교해서 나머지가 같거나 크면 단조증가하는수야
그럼 그 곱의 값을 맥시멈과 비교해서 크면 맥시멈 갱신
'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))

    maximum = -1
    for i in range(len(number)-1):
        for j in range(i+1, len(number)):
            tmp = number[i]*number[j]
            max_V = str(tmp)
            exist = True
            for j in range(len(max_V)-1):
                if int(max_V[j]) <= int(max_V[j+1]):
                    continue
                else:
                    exist = False
            if exist:
                if tmp > maximum:
                    maximum = tmp

    print('#{} {}'.format(tc, maximum))































