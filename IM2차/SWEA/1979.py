import sys
sys.stdin = open('1979.txt')


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    #가로 탐색
    result = 0
    for i in range(N):
        summation_x = 0
        for j in range(N):
            if board[i][j] == 1:
                summation_x += 1
            if board[i][j] == 0:
                if summation_x == K:
                    result += 1
                summation_x = 0
        if summation_x == K:
            result += 1

        summation_y = 0
        for j in range(N):
            if board[j][i] == 1:
                summation_y += 1
            if board[j][i] == 0:
                if summation_y == K:
                    result += 1
                summation_y = 0
        if summation_y == K:
            result += 1
    # for i in range(N):
    #     summation = 0
    #     for j in range(N):
    #         if board[j][i] == 1:
    #             summation += 1
    #         if board[j][i] == 0:
    #             if summation == K:
    #                 result += 1
    #             summation = 0
    #     if summation == K:
    #         result += 1
    print('#{} {}'.format(tc, result))
