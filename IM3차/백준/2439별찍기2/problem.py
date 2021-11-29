import sys
sys.stdin = open('input.txt')

N = int(input())

for i in range(N):
    tmp = ' ' * (N-i-1) + '*' * (i+1)
    print(tmp)
# arr = ['*'*N for _ in range(N)]
# # print(arr[0][0])
# for i in range(len(arr)):
#     for j in range(N-i-1):
#         arr[i].replace()
#
# for i in arr:
#     print(i)
