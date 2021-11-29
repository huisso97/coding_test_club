import sys
sys.stdin = open('input.txt')

T= int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    # 초기값 설정
    x = -1
    y = 0
    for num in range(1, N**2+1):
        if 0<=x<N and 0<=y<N and arr[x][y]==0:
            arr[x][y] = num


    print(arr)