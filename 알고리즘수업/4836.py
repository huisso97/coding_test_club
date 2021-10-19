T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*11 for _ in range(11)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for k in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[k][j] += color
    result = 0
    for i in range(11):
        for j in range(11):
            if arr[i][j] == 3:
                result += 1
    print('#{} {}'.format(tc, result))