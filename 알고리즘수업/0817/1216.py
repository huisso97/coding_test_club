import sys
sys.stdin = open('1216.txt')


for _ in range(10):
    tc = int(input())
    board = [list(input()) for _ in range(100)]

    for vertical in zip(*board):
        board.append(vertical)


    result = 0
    #행 처리
    for i in range(len(board)):
        #열처리
        #열의시작
        for k in range(100):
            #열의끝
            for j in range(1, 100):
                if board[i][k:k+j] == board[i][k:k+j][::-1]:
                    if result < len(board[i][k:k+j]):
                        result = len(board[i][k:k+j])
    print('#{} {}'.format(tc, result))