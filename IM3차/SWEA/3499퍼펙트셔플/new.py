import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(input().split())
    x = N // 2
    if N % 2 == 0:
        tmp1 = arr[:x]
        tmp2 = arr[x:]
        res = []
        for i in range(x):
            res.append(tmp1[i])
            res.append(tmp2[i])
    else:
        tmp1 = arr[:x + 1]
        tmp2 = arr[x + 1:]
        res = []
        for i in range(x):
            res.append(tmp1[i])
            res.append(tmp2[i])
        res.append(tmp1[-1])
    print('#{}'.format(tc), end=' ')
    print(*res)
