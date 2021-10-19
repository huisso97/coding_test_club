import sys
sys.stdin = open('5431.txt')
#
# T = int(input())
#
# for tc in range(1, T+1):
#     n, k = map(int, input().split())
#     submit = list(map(int, input().split()))
#     result = []
#     for num in range(1, n+1):
#         if num not in submit:
#             result.append(num)
#     print('#{}'.format(tc), end=' ')
#     for i in range(len(result)):
#         print(result[i], end=' ')
#     print()

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    result = []
    for i in range(1, N+1):
        if i not in submit:
            result.append(i)
    print('#{}'.format(tc), end=' ')
    for i in result:
        print(i, end=' ')
    print()













