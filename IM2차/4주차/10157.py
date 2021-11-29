import sys
sys.stdin = open('10157.txt')

C, R = map(int, input().split())
K = int(input())

#시계방향 상우하좌로 돌건데, 영역을 벗어나면 방향을 바꿀거야
#그런데 K값이 C*R보다 클 경우에는 0을 출력하고 멈출거야
#방문처리하면서 점점 좁게
#K 좌석 찾아
board = [[0]*C for _ in range(R)]

# print(visited)
x = 0
y = R

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
#
# for i in range(1, C*R+1):
if C*R < K:
    print(0)
else:
    idx = 0
    i = 1
    while i <= K:
        if idx > 3:
            idx = 0
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<C and 0<=ny<R and board[ny][nx]==0:
            #벽 안만났으면 방문 안했네
            board[ny][nx] = i
            x = nx
            y = ny
            i += 1
        else:
        #벽을 만났거나 방문했으면:
            idx += 1
    print(x+1,R-y)

# 시계방향 90도로 돌려서 행렬 만들어서 해보자
