import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

minimum = 2500
for i in range(N-7):
    for j in range(M-7):
        start = arr[i][j]
        cnt = 0
        # print(j)
        for m in range(4):
            for n in range(4):
                # print(row)
                # print(j+2*n)
                if start == 'W':
                    if arr[i+2*m][j+2*n] != 'W':
                        cnt += 1
                    if arr[i+2*m][j+2*n+1] != 'B':
                        cnt += 1
                    if arr[i+2*m+1][j+2*n] != 'B':
                        cnt += 1
                    if arr[i+2*m+1][j+2*n+1] != 'W':
                        cnt += 1
                elif start == 'B':
                    if arr[i+2*m][j+2*n] != 'B':
                        cnt += 1
                    if arr[i+2*m][j+2*n+1] != 'W':
                        cnt += 1
                    if arr[i+2*m+1][j+2*n] != 'W':
                        cnt += 1
                        # print(arr[i+2*m+1][j+2*n+1])
                        # print(i+2*m+1)
                        # print(j+2*n+1)
                    # print(arr[i+2*m][j+2*n+1])

                    if arr[i+2*m+1][j+2*n+1] != 'B':
                        cnt += 1
            # print(cnt)
        # print(cnt)
        if cnt < minimum:
            minimum = cnt
print(minimum)