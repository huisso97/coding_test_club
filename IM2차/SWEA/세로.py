import sys
sys.stdin = open('5356.txt')
T =int(input())
for tc in range(1, T+1):
    board = []
    maximum = 0
    for i in range(5):
        arr = list(input())
        if len(arr)>maximum:
            maximum = len(arr)
        board.append(arr)
    print('#{}'.format(tc),end=' ')

    for i in range(maximum):
        for j in range(5):
            try:
                print(board[j][i], end='')
            except:
                pass
    print()