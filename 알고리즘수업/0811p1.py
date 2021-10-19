import sys
sys.stdin = open('0811p1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # print(board)
    for y in range(N):
        for x in range(N):
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<N and 0<=ny<N:
                    result += abs(board[y][x]-board[ny][nx])

    print('#{} {}'.format(tc, result))

    # 2
    arr = [[0] * n for _ in range(n)]
    # print(arr)

    # 방향 벡터 우 하 좌 상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 범위는 n*n까지
    for i in range(n ** 2):
        # x의 범위는 오른쪽으로 가면서 벽만나면 다시 0 되므로 n으로 나눈 나머지이고
        # y의 범위는 x가 오른쪽 끝까지 도달하면 +1 되므로 n으로 나눈 몫이 된다.
        x = i % n
        y = i // n
        # 4 방위로 다 계산 한 값을 찾기 위해 for문은 4번돌리고
        for mode in range(4):
            # 돌아가면서 들어오는 mode값을 방향벡터로 넣어 사용한다.
            nx = x + dx[mode]
            ny = y + dy[mode]
            # 벽을 만나지 않을 때 까지 계산한 값을 해당 배열에 넣어주고
            if n > nx >= 0 and n > ny >= 0:
                arr[y][x] += abs(data[ny][nx] - data[y][x])
    # 원하는 값 출력
    print(arr)
    result = 0
    for i in arr:
        result += sum(i)
    # print('#{} {}'.format(tc, sum(arr)))
    print(result)