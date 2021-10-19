import sys
sys.stdin = open('1954.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dx = [1, 0 ,-1, 0]
    dy = [0, 1, 0, -1]


    arr = [[0]*N for _ in range(N)]
    # print(arr)
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
            idx +=1
        else:
            idx = 0
    print('#{}'.format(tc))
    for i in arr:
        print(*i)

'''관이꼬
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)] # [[0]*n]*n은 왜 안되는가?

    # 우 하 좌 상 방향 설정
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 방향벡터 설정을 위한 mode
    mode = 0 # idx
    x = 0
    y = 0
    # 숫자 1부터 n*n까지 넣어줄 것이기 때문에 range 범위는 1부터 n**2의 +1 까지 지정
    for i in range(1, n**2+1):
        # 시작 지점인 arr[0][0]에 1을 넣고 시작 그리고 돌면서 방향벡터로 이동한 곳에
        # 하나씩 숫자를 증가시켜서 그 값을 넣어준다.
        arr[y][x] = i
        # 방향벡터로 좌표값 움직여준다.
        x += dx[mode]
        y += dy[mode]
        # 방향벡터를 사용할 때 가장 중요한 점은 n*n 행렬 범위를 벗어나서는 안되고 이미 값이 들어있는 곳에
        # 다른 값을 넣으면 안되기 때문에, 각 행렬의 끝을 벗어나거나 이미 입력된 값을 만나면
        # 벽이라고 인식하고 방향을 바꿔주기 위해 조건문을 아래와 같이 설정한다.
        if n > x + dx[mode] >= 0 and n > y + dy[mode] >= 0 and not arr[y+dy[mode]][x+dx[mode]]:
            # 이게 가장 핵심인데, 아직 그 방향으로 나아갈 수 있으면 이라는 조건이 위에서 통과되면,
            # 방향벡터를 수정하지 않고 그 방향으로 유지를 해야되기 때문에 아래 if문을 실행시키지 않기 위해
            # continue를 사용해 값을 입력하는 반복문을 다시 시작하게 된다.
            continue
        # 1
        # if mode != 3:
        #     mode += 1
        # else:
        #     mode = 0
        # 2
        mode = (mode+1)%4
    print('#{}'.format(tc))
    for i in arr:
        print(*i)
'''
