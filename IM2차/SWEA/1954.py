import sys
sys.stdin = open('1954.txt')

T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list([0]*N) for _ in range(N)]
#
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     idx = 0
#     x = 0
#     y = 0
#     for i in range(1, N**2+1):
#         arr[y][x] = i
#         x += dx[idx]
#         y += dy[idx]
#         if 0<=x+dx[idx]<N and 0<=y+dy[idx]<N and not arr[x+dx[idx]][y+dy[idx]]:
#             continue
#         if idx !=3:
#             idx+=1
#         else:
#             idx = 0
#     print(arr)

for tc in range(1, T+1):
    N = int(input())
    arr = list([0]*N for _ in range(N))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x = 0
    y = 0
    idx = 0
    for i in range(1, N**2+1):
        arr[y][x] = i
        x += dx[idx]
        y += dy[idx]
        # print(nx, ny)
        if 0<=x+dx[idx]<N and 0<=y+dy[idx]<N and not arr[y+dy[idx]][x+dx[idx]]:
            continue
        if idx != 3:
            idx += 1
        # ㄱ,람
        # 그럼
        # 보지마
        # 맛도리
        else:
            idx = 0
    print('#{}'.format(tc))
    for i in arr:
        #ㅎㅎㅎㅎ.........,,,,,,,,,,,,, 죄.....솓ㅇ......합니다...
        #ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ
        #나는 다 계산을 했지
        #ㅎㅂㅎ
        print(*i)
        #Arigatto..........
        #u r since
        #wow............
        #naega jiqeum ireoke beer drink haneungeo beuloji?
        #since others do their bests but i'm not
        #right?
        #geurae.......................
        #ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        #oppa neun
        #anmasilgeo?
        #neo whyiri kind?
        #oppa hoxi
        #my house come eba?
        #eba ....
        #yes....
        #you have exam tomorrow
        #wow

















