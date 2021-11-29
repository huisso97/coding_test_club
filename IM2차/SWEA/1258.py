import sys
sys.stdin = open('1258.txt')

# def Check(idx, tmp_x):
#     tmp_xx = []
#     if idx == len(board)-1:
#         return
#     exist = True
#     #tmp_x의 열길이 만큼 행 전체 체크
#     for i in range(idx+1, len(board)):
#         for j in range(len(tmp_x)):
#             if board[i][j] != 0:
#                 tmp_xx.append(board[i][j])
#             else:
#                 tmp.append(tmp_xx)
#                 Check(i+1, tmp_x)
#         if board[i] == 0:
#             exist = False
#             break
#     if exist == False:
#         return
#
# T= int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#
#     result = []
#     tmp = []
#     for i in range(len(board)):
#         tmp_x = []
#         for j in range(len(board)):
#             if board[i][j] != 0:
#                  tmp_x.append(board[i][j])
#                  print(board[j][i])
#             else:
#                 tmp.append(tmp_x)
#                 Check(i, tmp_x)
#                 result.append(tmp)
#                 tmp_x = []
#
#     print(tmp)

def clear(sty,stx):
    edx = stx
    edy = sty
    for y in range(sty, N):
        for x in range(stx, N):
            board[y][x] = 0
            #x축으로 0이 나오거나 끝이면 break
            if board[y][x+1] == 0 or x+1 == N:
                break
        edx = x
        #y축으로 0이 나오거나 끝이면 break
        if board[y+1][x] == 0 or y+1 == N:
            break
    edy = y
    result.append((edy-sty+1, edx-stx+1))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]


    result = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                clear(i, j)
    result.sort(key=lambda x:x[0]*x[1])

    print(result)





