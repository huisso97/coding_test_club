import sys
sys.stdin = open('4466.txt')

# def Find():
#     global maximum, result, K
#     if len(result) == K:
#         if maximum < sum(result):
#             maximum = sum(result)
#             return
#     else:
#         for j in range(0, len(lst)):
#             if lst[j] not in result:
#                 result.append(lst[j])
#                 Find()
#                 result.pop()
# 

T =int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    print('#{} {}'.format(tc, sum(lst[:K])))