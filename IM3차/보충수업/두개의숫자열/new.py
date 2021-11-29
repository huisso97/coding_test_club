import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maximum  = 0
    if N > M:
        for i in range(N-M+1):
            tmp = 0
            for j in range(M):
                # print(A[i])
                # print('--')
                # print(A[i+j])
                tmp += A[i+j]*B[j]
            if tmp > maximum:
                maximum = tmp
    else:
        for i in range(M-N+1):
            tmp = 0
            for j in range(N):
                tmp += B[i+j] * A[j]
            if tmp > maximum:
                maximum = tmp
    print('#{} {}'.format(tc, maximum))