import sys
sys.stdin = open('1220.txt')


for tc in range(1, 11):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(length)]
    # print(board)
    board = []
    for vertical in zip(*arr):
        board.append(vertical)
    cnt = 0

    # print(len(board))
    for i in range(length):
            #뒤에 아무것도 없어야해 그치?
        idx = 0
        while True:
            # print(i, idx)
            # print(board[i][idx])
            if board[i][idx] == 1:
                for k in range(idx+1, len(board)):
                    if board[i][k] == 2:
                        cnt += 1
                        idx = k
                        break
            if idx == len(board)-1:
                break
            idx += 1
    print(cnt) 
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    cnt = 0
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n-1):
        for j in range(n):
            if arr[i][j] == 1:
                if arr[i+1][j] == 2:
                    cnt += 1
                # k라는 임시변수를 이용해서 j로 고정해놓고 2가 나올때까지
                # 이동해준 것
                #
                elif arr[i+1][j] == 0:
                    arr[i+1][j] = arr[i][j]
    print('#{} {}'.format(tc, cnt))