import sys
sys.stdin = open('1859.txt')

# def Find(idx):
#     global buy, profit
#     #기저
#     if idx == N-1:
#         profit = max(maximum, profit)
#         return
#     #사기
#     profit -= arr[idx]
#     buy[idx] = True
#     Find(idx+1)
#     #원상복구
#     profit += arr[idx]
#     buy[idx] = False
#
#     #팔기
#     cnt = 0
#     for i in buy:
#         if i:
#            cnt += 1
#     profit += arr[idx]*cnt
#     for i in buy:
#         if i:
#             i = False
#     Find(idx+1)
#     #원상복구
#     profit -= arr[idx]*cnt
#     for i in range(cnt):
#         buy[i] = True
for i in range(N):
    if isSel[i] == 1:
        profit -= lst[i]
    elif isSel[i] == 2:
            idx = i-1
        while idx!=0 or idx!=2:
            profit += lst[idx]
            idx -= 1
#
# def setIsSel(flag, pos):
#     global profit,
#     if isSel[pos]*len(arr[:pos]) > profit:
#         profit = isSel[pos]*len(arr[:pos])
#
#         #사겠다
#         for j in range(flag, pos):
#             isSel[j] = 1
#         #팔겠다
#         isSel[pos] = 2
#     else:
#         isSel[pos] = 1


T = int(input())
T = 3
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    maximum = 0
    profit = 0
    isSel = [0]*N
    # for i in range(1, N):
    #     if arr[i-1] < arr[i]:
    #         setIsSel(flag, i)



for i in range(N, -2, -1):
    if arr[i] > arr[i-1]:
        profit = arr[i]-arr[i-1]
    #
print(profit)
    #
    # else:
    #     continue