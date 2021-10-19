C, R = map(int, input().split())
K = int(input())

arr = [[0]*C for _ in range(R)]
y = R
x = 0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
if K > C*R:
    print(0)
else:
    idx = 0
    num = 1
    # arr[x][y] = num
    while num <= K:
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<C and 0<=ny<R and arr[ny][nx]==0:
            arr[ny][nx] = num
            num += 1
            x = nx
            y = ny
            continue
        if idx != 3:
            idx += 1
        else:
            idx = 0
    print(x+1, R-y)
