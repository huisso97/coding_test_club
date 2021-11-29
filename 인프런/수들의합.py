import sys
sys.stdin = open('in1.txt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# l = 0
# r = 1
# summation = arr[l]
# cnt = 0
# while l != r:
#     if summation == m:
#         cnt += 1
#         l += 1
#         r = l+1
#     else:
#         summation += arr[r]
#         r += 1
# print(cnt)
cnt = 0
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += arr[j]
        if tmp == m:
            cnt += 1
            break
        # tmp = sum(arr[i:j+1])
        # if tmp == m:
        #     cnt += 1
        #     break
print(cnt)
