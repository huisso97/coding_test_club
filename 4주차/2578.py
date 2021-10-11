import sys
sys.stdin = open('2578.txt')

board = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
visited = [list(False for _ in range(5)) for _ in range(5)]
number = []
for i in range(5):
    for j in range(5):
        number.append(mc[i][j])

cnt = 0
for i in range(len(number)):
    check = number[i]
    bingo = 0
    for m in range(len(board)):
        for n in range(len(board)):
            if visited[m][n] == True:
                bingo += 1
            elif visited[n][m] == True:
                bingo
            elif visited[n][m] == True:
                pass
            elif visited[n][m] == True:
                pass
            if check == board[m][n]:
                visited[m][n] = True
                cnt += 1
