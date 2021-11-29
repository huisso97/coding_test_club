import sys
sys.stdin = open('sample_input.txt')

T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maximum = -1
    num_list = [i for i in range(1000)]
    # print(num_list)
    lst = []
    for sy in range(N):
        for sx in range(N):
            start = arr[sy][sx]
            big = 0
            idx_list = []
            exist = False
            for i in range(N-1, sy, -1):
                for j in range(N-1, sx, -1):
                    number = arr[i][j]
                    if start == number:
                        # print(sx, sy, j , i)
                        for k in range(len(lst)):
                            if sum(lst[k][0]) == sx+sy+i+j:
                                exist = True
                                break
                        big = ((abs(sy-i)+1)*(abs(sx-j)+1))
                        idx_list = [sy, sx, i, j]
                        # print(i, j)

                if exist:
                    exist = False
                    break
                # print(big)
                if big >= maximum:
                    maximum = big
                    lst.append([idx_list, big])
        num_list = [i for i in range(1000)]
    # print(lst)
    num_list1 = [i for i in range(100)]
    # print(num_list)
    maximum = lst[-1][-1]
    cnt = 0
    for i in range(len(lst)):
        if lst[i][-1] == maximum:
            cnt += 1
    # print(cnt)
    cnt = 0
    for sy1 in range(N):
        for sx1 in range(N):
            start1 = arr[sy1][sx1]
            if start1 in num_list1:
                num_list1.remove(start1)
                big = 0
                for i in range(N-1, sy-1, -1):
                    for j in range(N-1, sx-1, -1):
                        number = arr[i][j]
                        if start1 == number:
                            big = ((abs(sy1 - i) + 1) * (abs(sx1 - j) + 1))
                            if maximum == big:
                                cnt += 1
    print('#{} {}'.format(tc, cnt))
