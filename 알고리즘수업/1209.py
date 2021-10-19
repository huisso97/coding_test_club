import sys
sys.stdin = open('1209.txt')

for _ in range(1, 11):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    maximum = 0
    tmp_d1 = 0
    tmp_d2 = 0
    for i in range(100):
        tmp_x = 0
        tmp_y = 0
        tmp_d1 += board[i][i]
        tmp_d2 += board[i][100-i-1]
        for j in range(100):
            tmp_x += board[i][j]
            tmp_y += board[j][i]
        if tmp_x > maximum:
            maximum = tmp_x
        if tmp_y > maximum:
            maximum = tmp_y
    if tmp_d1 > maximum:
        maximum =tmp_d1
    if tmp_d2 > maximum:
        maximum = tmp_d2
    print('#{} {}'.format(tc, maximum))


