import sys
sys.stdin = open('1954.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    cnt = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    x = -1
    y = 0
    while cnt <= N**2:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<N and 0<=ny<N and arr[ny][nx]==0:
            arr[ny][nx] = cnt
            cnt += 1
            x = nx
            y = ny
            continue
        if idx !=3:
            idx += 1
        else:
            idx = 0
    print('#{}'.format(tc))
    for i in arr:
        print(*i)
    # print('#{} {}'.format(tc, *arr))