import sys
sys.stdin = open('2001.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    tmp = []
    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            sub = 0
            maximum = 0
            for x in range(m):
                for y in range(m):
                    sub += arr[i+x][j+y]
            if sub > maximum:
                maximum = sub
                tmp.append(maximum)

    print('#{} {}'.format(tc, max(tmp)))