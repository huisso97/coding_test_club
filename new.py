import sys
sys.stdin = open('sample_input.txt')
T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maximum = -1
    num_list = [i for i in range(1000)]
    # print(num_list)
    for sy in range(N):
        for sx in range(N):
            start = arr[sy][sx]
            # if start in num_list:
            #     num_list.remove(start)
            big = 0
            lst = []
            for i in range(N):
                for j in range(N):
                    number = arr[i][j]
                    if start == number:
                        # print(sx, sy, j , i)
                        big = ((abs(sy-i)+1)*(abs(sx-j)+1))
                        lst.append([sy, sx, i,j, big])
                        # print(big)
            print(lst)
            if big > maximum:
                maximum = big
    # print(maximum)
    num_list1 = [i for i in range(100)]
    # print(num_list)
    cnt = 0
    for sy1 in range(N):
        for sx1 in range(N):
            start1 = arr[sy1][sx1]
            # if start1 in num_list1:
            #     num_list1.remove(start1)
            big = 0
            for i in range(N):
                for j in range(N):
                    number = arr[i][j]
                    if start1 == number:
                        big = ((abs(sy1 - i) + 1) * (abs(sx1 - j) + 1))
                        if maximum == big:
                            cnt += 1
    print('#{} {}'.format(tc, cnt))