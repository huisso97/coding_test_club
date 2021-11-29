import sys
sys.stdin = open('2001.txt')

# T = int(input())
#
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     tmp = []
#     for i in range(0, n-m+1):
#         for j in range(0, n-m+1):
#             sub = 0
#             maximum = 0
# #             for x in range(m):
# #                 for y in range(m):
# #                     sub += arr[i+x][j+y]
# #             if sub > maximum:
# #                 maximum = sub
# #                 tmp.append(maximum)
# #
# #     print('#{} {}'.format(tc, max(tmp)))
# #
# #
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     maximum = 0
#     fly = 0
#     idx = 0
#     x = 0
#     y = 0
#     while y+M != N+1:
#         for i in range(y, y+M):
#             for j in range(x, x+M):
#                 fly += board[i][j]
#             if fly > maximum:
#                 maximum = fly
#         x+=1
#         fly = 0
#         if x == N-M+1:
# #             x = 0
# #             y += 1
# #     print('#{} {}'.format(tc, maximum))
# # '''
# T = int(input())
#
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     fly_r = [list(map(int, input().split())) for _ in range(n)]
#     # 기존에 있는 배열의 세로줄을 가로줄로 변환해주는 zip(*list)
#     # zip을 통해 나온 튜플을 list로 변환해주는 map(list)
#     fly_c = list(map(list, zip(*fly_r)))
#     print(fly_c)
#     max_v = 0
#     # 첫번째 줄부터 계산해주기 위해 고정하는 i
#     for i in range(n-m+1):
#         # 하나씩 오른쪽으로 이동해서 검색할 j
#         for j in range(n-m+1):
#             # 임시로 계산된 값들을 담아줄 변수 초기화
#             tmp = 0
#             # 원하는 m 개수만큼 슬라이싱 해줄 k
#             for k in range(m):
#                 # 슬라이싱으로 필요한 부분을 가져와서 더해준다.
#                 tmp += sum(fly_r[i+k][j:j+m])
#                 print(fly_r[i+k][j:j+m])
#             # 임시 계산 값과 기존에 들어있는 최대값 비교
#             if tmp > max_v:
#                 max_v = tmp
#     print('#{} {}'.format(tc, max_v))

'''
    # while True:
    #     if N-M+idx+1 == N:
    #         break
    #     for i in range(N-M+1+idx):
    #         tmp = 0
    #         while True:
    #             if N-M+1+tmp == N:
    #                 break
    #             for j in range(N-M+1+tmp):
    #                 fly += board[i][j]
    #             tmp += 1
    #             if fly > maximum:
    #                 maximum = fly
    #         if fly > maximum:
    #             maximum = fly
    #     idx += 1
    # print(maximum)

'''
T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    fly = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            result = 0
            for i in range(x, M+x):
                for j in range(y, M+y):
                    # fly += board[i][j:j+M]
                    result+=board[i][j]
            if maximum < result:
                maximum = result
    print('#{} {}'.format(tc, maximum))
















































