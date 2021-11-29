import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    N, M  = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for m in range(M):
                for n in range(M):
                    tmp += arr[i+m][j+n]
            if tmp > maximum:
                maximum = tmp
    print('#{} {}'.format(tc, maximum))
