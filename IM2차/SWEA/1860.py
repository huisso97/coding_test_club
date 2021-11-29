import sys
sys.stdin = open('1860.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     #제일 늦게 도착한 사람의 시간까지 붕어빵을 미리 시간대별로 만들기
#     #시간에 맞춰 사람들이 먹을 수 있으면 pass
#     #안되면 impossible
#     people = list(map(int, input().split()))
#     time = max(people)
#     #0번째 인덱스 무시하기
#     fish = [0]*(time+1)
#     for i in range(1, (time)//M+1):
#         fish[M*i] = K
#
#     guest = [0]*(time+1)
#     for i in range(len(people)):
#         arrive = people[i]
#         # print(people[i])
#         guest[arrive] += 1
#     # print(fish)
#     # print(guest)
#     exist = True
#     for i in range(len(fish)):
#         if sum(fish[:i])<sum(guest[:i]):
#             print('#{} {}'.format(tc, 'Impossible'))
#             exist = False
#             break
#     if exist:
#         print('#{} {}'.format(tc, 'Possible'))

T = int(input())
for tc in range(1, T+1):
    # N: 사람수, M초의 시간을 들이면 K개의 붕어 만들수있음
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time.sort()

    result = "Possible"
    # x초까지 만들어진 붕어 개수: (x // M) * K
    for i in range(N):
        boong = (arrive_time[i] // M) * K - (i+1)
        if boong < 0:
            result = "Impossible"
            break
        boong = (arrive_time[i] // M) * K - (i+1)
                #손님 도착시간 // 내가 만드는데 걸리는 시간 * 갯수 - 지금까지 손님 수


    print("#{} {}".format(tc, result))
T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    bread = k
    result = ''
    for i in range(n):
        tmp = customer[i]
        hap = (tmp // m) * k
        if hap > i + 1:
            result = 'Possible'
            continue
        if hap < i + 1:
            result = 'Impossible'
            break
    print('#{} {}'.format(tc, result))
