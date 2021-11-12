import sys
sys.stdin = open('sample_input.txt')
T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maximum = -1
    lst = []
    num_list = [i for i in range(100)]
    # print(num_list)
    for sy in range(N):
        for sx in range(N):
            start = arr[sy][sx]
            big = 0
            if start in num_list:
                num_list.remove(start)
                for i in range(N-1, -1, -1):
                    for j in range(N-1, -1, -1):
                        number = arr[i][j]
                        if start == number:
                            # print(sx, sy, j , i)
                            big = ((abs(sy-i)+1)*(abs(sx-j)+1))
                            print(big)
            if big > maximum:
                maximum = big
                lst.append(maximum)
    print(lst)
    print('done', maximum)