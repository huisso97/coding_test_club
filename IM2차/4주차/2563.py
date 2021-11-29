import sys
sys.stdin = open('2563.txt')

N = int(input())
#[[3, 7], [15, 7], [5, 2]] 열, 행
paper = []
board = [[0]*30 for _ in range(30)]
cnt = 0
for i in range(N):
    paper.append(list(map(int, input().split())))
    x = paper[i][0]
    y = paper[i][1]

    for m in range(y, y+10):
        for n in range(x, x+10):
            if board[m][n] == 1:
                continue
            board[m][n] = 1
            cnt += 1
print(cnt)
