import sys
sys.stdin = open('11866.txt')

n , k = map(int, input().split())


arr = [i+1 for i in range(n)]
#arr=[1,2,3,4,5,6,7]
#arr=[1,,,,,,]
result = []
start_idx = k-1
while len(arr) != 0:

    if start_idx >= len(arr): #우리가 찾고자하는 숫자를 변경되지 않은채, 최소화한다. 1바퀴 돌린다는 개념
        start_idx -= len(arr)
    else:
        result.append(arr.pop(start_idx))
        start_idx += k-1

    #     start_idx %= k + 1
    #     result.append(arr.pop(start_idx))
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>')



# arr = [False]+[i+1 for i in range(n)]
#
# result = []
# idx = 0
# while len(result) < n:
#     idx += k
#     # +k인덱스 했는데 len초과하면 더한값의 * n 의 인덱스 접근
#     if idx >= len(arr):
#         idx = idx % n
#         if arr[idx] == 0:
#             while arr[idx] == True:
#                 idx += 1
#         else:
#             result.append(arr[idx])
#             arr[idx] = 0
#     #리스트 길이 내의 인덱스는 직접 접근하되, 방문안한 애들만 체크
#     else:
#         if arr[idx] == 0:
#             while arr[idx] == True:
#                 idx += 1
#         else:
#             result.append(arr[idx])
#             arr[idx] = 0
#     print(idx)
# #
# n , k = map(int, input().split())
#
# arr = [0]+[i+1 for i in range(n)]
# result = []
# idx = 0
# while len(result) < n:
#     idx += k
#     # +k인덱스 했는데 len초과하면 더한값의 * n 의 인덱스 접근
#     if idx >= len(arr):
#         idx = idx % n
#         result.append(arr.pop(idx))
#     #리스트 길이 내의 인덱스는 직접 접근하되, 방문안한 애들만 체크
#     else:
#         result.append(arr.pop(idx))
#     print(idx)