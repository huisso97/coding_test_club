#열/행/3*3 구간을 체크할거야
#1~9 인덱스에 False를 두고
# False면 True
# True인데 또 접근하려고 하면
# 한 구간에 중복되는 숫자가 있으니 print(0) exist = False
# exist 가 True이면
# print(1)
import sys
sys.stdin = open('1974.txt')

T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    exist = True
    # 열 탐색
    number = [0 for _ in range(10)]
    for i in range(len(board)):
        for j in range(len(board)):
            check = board[i][j]
            number[check] += 1
            # print(number)
            if number[check] != 1:
                exist = False
                break
        number = [0 for _ in range(10)]

    # 행 탐색
    for i in range(len(board)):
        for j in range(len(board)):
            check = board[j][i]
            number[check] += 1
            # print(number)
            if number[check] != 1:
                exist = False
                break
        number = [0 for _ in range(10)]

    # 3*3 탐색
    for x in range(0, len(board), 3):
        for y in range(0, len(board), 3):
            for i in range(3):
                for j in range(3):
                    check = board[j][i]
                    number[check] += 1
                    # print(number)
                    if number[check] != 1:
                        exist = False
                        break
            number = [0 for _ in range(10)]

    if exist:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
    # idx = 0
    # while True:
    #     if idx > 6:
    #         break
    #     tmp = 0
    #     while True:
    #         if tmp > 6:
    #            break
    #         for i in range(idx, idx+3):
    #             for j in range(tmp, tmp+3):
    #                 check = board[i][j]
    #                 number[check] += 1
    #                 # print(number)
    #                 if number[check] == 2:
    #                     exist = False
    #                     break
    #         tmp += 3
    #         number = [0 for _ in range(10)]
    #     idx += 3
