import sys
sys.stdin = open('10157.txt')

C, R = map(int, input().split())
K = map(int, input().split())
#보드판 행 뒤집어
#시계방향 상우하좌
#K 좌석 찾아
board = [[0]*(C) for _ in range(R)]
visited = [[False]*(C) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
i = 1
for x in range(len(board)):
    for y in range(len(board)):
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<len(board) and 0<=ny<len(board) and visited[nx][ny] == False:
                while True:
                    board[nx][ny] = i
                    if i == K:
                        print(nx, ny)
                    i += 1

                    visited[nx][ny] = True

# i = 1
# while True:
#     if i == K:
#         pass
#     i+=1