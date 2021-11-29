import sys
sys.stdin = open('전기버스.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
#
#     station = [False for _ in range(N+1)]
#     #정류장 표시
#     for i in temp:
#         station[i] = True
#     # while True:
#         # your
#         # if 무언가가 K보다 작으면:
#         # 일단 다 가고 뒤에서부터 체크
#         # 존나 어렵네  마음의 소리
#         # 최고다
#         # 그 날
#         # 제일 마음에
#         # 난 진
#         # 충전기 만났어
#         # 그럼 충전~
#         # 근데 다시 시작지점에서 만나면 넌 아웃!
#         # 지금 우리는 너무 달렸다
#         # 우리 14분 노가리 까자
#         # 노가리 타임
#         # 네!!!!
#     # 존경해 respect 살신성인 태도가 이런 각박하고 자기 안위를 챙기는 세상에서
#     # 지금 이 싸피 공간이 그렇진 않지만,
#     # 나는 존나 어려
#     # 난 .........
#     # 마디토 madito
#     # 웃기네잉!
#     #
#     ##버스 출발 위치
#     idx = 0
#     cnt = 0
#     exist = False
#     flag = 1
#     while flag:
#         pre_pos = idx
#         idx += K
#         if idx >= N:
#             print('#{} {}'.format(tc, cnt))
#             break
#         if station[idx] == True:
#            cnt += 1
#         else:
#             while idx != :
#                 if idx == pre_pos:
#                     break
#                 idx -= 1
#                 if station[idx] == True:
#                     cnt += 1
#                     break
#             else:
#                 print('#{} {}'.format(tc, 0))
#                 flag = 0
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for k in range(1, T + 1):
    K, N, M = map(int, input().split())
    temp = list(map(int, input().split()))

    station = [False for i in range(N + 1)]
    for i in temp:
        station[i] = True

    idx = 0
    cnt = 0
    flag = 1 #스위치 킨거야

    while flag:
        pre_pos = idx   # 이전위치
        idx += K        # 쩜프한 위치
        if idx >= N:    # 도착했으면 프린트
            print('#{} {}'.format(k, cnt))
            break

        if station[idx]:    # 쩜프한자리에 충전소가있으면 그냥 충전하고 진행
            cnt += 1
        else:
            while idx != pre_pos:   # 내가 쩜프하기 전 위치가 될때까지 한칸씩 뒤로가
                idx -= 1
                if station[idx] and idx != pre_pos:  # 만약 그자리에 충전소가 있어? 그럼충전해, 대신 시작위치 충전소 말고
                    cnt += 1
                    break
            else:
                print('#{} {}'.format(k, 0))    # 안되는 경우면 flag 0 (안되네? 스위치 꺼야지 맨 위 while문 종료해야지)
                flag = 0

'''

# T = int(input())
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     charge = list(map(int, input().split()))
#     station = [False for _ in range(N+1)]
#     for i in charge:
#         station[i] = True
#
#     pre_start = 0
#     now = 0
#     cnt = 0
#     while True:
#         #
#         if station[i]:
#             pre_start = i
#             now = pre_start+K
#             exist = False
#             while now != pre_start:
#                 if station[now]:
#                     cnt += 1
#                     exist = True
#                 now -= 1
#             if exist == False:
#                 print('#{} {}'.format(tc, 0))


    # print('#{} {}'.format(tc, result))


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    station = [False for _ in range(N+1)]
    for i in range(len(charge)):
        station[charge[i]] = True
    #시작지점(변수선언)
    past = 0
    now = past+K
    cnt = 0
    # exist = True
    while True:
        # 충전가능하면 거기서 충전 N은 종점이였다....
        if now >= N:
            break
        if station[now]: 
            cnt += 1
            past = now
            now = past + K
        else:
            now -= 1
            # 뺐는데 자기자리네
            if past == now:
                cnt = 0
                # print('#{} {}'.format(tc, 0))
                # exist = False
                break
            continue
    print('#{} {}'.format(tc, cnt))

#####################관##############################
K, N, M = map(int, input().split())
charge_list = list(map(int, input().split()))
stations = [0] * (N)
# 주유소를 표시
for i in charge_list:
    stations[i] = True
# print(stations)

cnt = 0
now = K
# 연료
energy = K

while True:
    if now >= N:
        break
        # 주유소 있다
    if stations[now] == True:
        # 그럼 충전하자
        cnt += 1
        # 현재위치는 K만큼 더 이동할거고
        now += K
        # 에너지는 K로 충전될거다
        energy = K
        # 주유소 없다
    elif stations[now] == False:
        # 현재위치는 하나 뒤로 보내서 주유소 찾는다
        now -= 1
        # 간만큼 연료 줄어든다
        energy -= 1
        # 근데 연료가 0이 돼버린다.
        # 제자리를 반복하고 있다.
        if energy <= 0:
            # 그럼 충전을 해도 의미 없으니까
            # 문제에서 제시한대로 충전횟수를 0으로 바꿔주고
            cnt = 0
            # 반복문을 종료한다.
            break
# 최종 충전횟수 출력해준다.
print('#{} {}'.format(tc, cnt))
















