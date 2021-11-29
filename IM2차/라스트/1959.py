import sys
sys.stdin = open('1959.txt')


T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    maximum = 0
    if N>=M:
        for i in range(N-M+1):
            result = 0
            for j in range(M):
                result += A[i+j] * B[j]
            if maximum < result:
                maximum = result
    elif N<M:
        for i in range(M-N+1):
            result = 0
            for j in range(N):
                result += B[i+j] * A[j]
            if maximum < result:
                maximum = result
    print('#{} {}'.format(tc, maximum))