import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    base = N//2
    cnt = 0
    for i in range(N//2):
        # print(i)
        # print(base)/
        for j in range(N//2-i, N//2+i):
            print(arr[i][j])
        # for j in range(N//2, N//2+1):
        #     print(arr[i][j])
            # cnt += arr[i][j]
            # cnt += arr[N - i - 1][j]
    # for i in range(N//2+1):
    #     for j in range(base-i, base+i+1):
    #         cnt += arr[N-i-1][j]