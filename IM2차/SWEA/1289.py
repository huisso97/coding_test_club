import sys
sys.stdin = open('1289.txt')

#
# T= int(input())
# for tc in range(1, T+1):
#     number = list(input())
#
#     origin = ['0'] * len(number)
#     exist = False
#     cnt = 0
#     while True:
#         if exist:
#             print('#{} {}'.format(tc, cnt))
#             break
#         for i in range(len(number)):
#             if number == origin:
#                 exist = True
#                 break
#             if number[i] == '1':
#                 if origin[i] == '0':
#                     for j in range(i, len(number)):
#                         origin[j] = '1'
#                     cnt +=1
#             else:
#                 if origin[i] == '1':
#                     for j in range(i, len(number)):
#                         origin[j] = '0'
#                     cnt +=1
        # print(origin)
        # 웅!
        # 웅웅@@@@@@@@@@@@!!!!!!!!!!!!!!
        # 알게쏘~!!!!!!!!!!!!!!!!!!!!!!!
        # 구래!
        #

T = int(input())

for tc in range(1, T+1):
    # 원래 메모리
    memory = list(map(int, input()))
    # 초기화 메모리
    now = [0] * len(memory)
    # 교환 횟수
    cnt = 0
    # 일단 모든 memory를 비교해야되므로 memory길이만큼 반복문을 돌린다
    for i in range(len(memory)):
        # 만약 초기화된 메모리 첫번째 bit와 원래 메모리 첫번째 bit가 다르면
        if memory[i] != now[i]:
            # 교환 횟수가 1 증가하고
            cnt += 1
            # i번째 이후 bit를 모두 원래 메모리 값으로 다 변환시켜준다.
            for j in range(i, len(memory)):
                now[j] = memory[i]
            # 만약 원래 메모리 값과 초기화된 메모리를 변경한 값이 같으면
            # 원래 메모리 값으로 돌아온 것이므로 반복문 종료
            if memory == now:
                break
    # 최종 출력값인 교환 횟수 출력
    print('#{} {}'.format(tc, cnt))
    print(memory)