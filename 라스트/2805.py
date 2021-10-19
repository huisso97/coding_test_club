# import sys
# sys.stdin = open('2805.txt')

T =int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [list(map(int, input())) for _ in range(N)]

    length = N//2

    result = 0

    for i in range(N//2+1):
        tmp = board[i][N//2-i:N//2+i+1]
        result+=sum(tmp)
    for i in range(N//2):
        tmp = board[N-i-1][N//2-i:N//2+i+1]
        result += sum(tmp)
    print('#{} {}'.format(tc, result))
    