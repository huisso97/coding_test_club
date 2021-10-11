import sys
sys.stdin = open('3085.TXT')

n = int(input())

board = [list(input()) for _ in range(n)]
# print(board)
maximum = 0
#행 체크
def width(board):
    global maximum

    for x in range(len(board)):
        cnt = 1
        for y in range(len(board)-1):
            #한줄의 사탕이 다를 경우
            if board[x][y] == board[x][y+1]:
                cnt += 1
            else:
                if maximum < cnt:
                    maximum = cnt
                # cnt = 1
        # 한 줄이 다 같을 경우
        if maximum < cnt:
            maximum = cnt

def height(board):
    global maximum

    for x in range(len(board)):
        cnt = 1
        for y in range(len(board)-1):
            #한줄의 사탕이 다를 경우
            if board[y][x] == board[y+1][x]:
                cnt += 1
            else:
                if maximum < cnt:
                    maximum = cnt
                #중간에 끊겼으니 다시 처음부터 세야지
                cnt = 1
        # 한 줄이 다 같을 경우
        if maximum < cnt:
            maximum = cnt


#가로 바꾸기
for i in range(len(board)):
    for j in range(len(board)-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        #전체 행 체크
        width(board)
        #전체 열 체크
        height(board)
        board[i][j], board[i][j + 1] = board[i][j], board[i][j + 1]
#세로 바꾸기
for i in range(len(board)):
    for j in range(len(board)-1):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        # 전체 행 체크
        width(board)
        # 전체 열 체크
        height(board)
        board[j][i], board[j + 1][i] = board[j][i], board[j + 1][i]

print(maximum)