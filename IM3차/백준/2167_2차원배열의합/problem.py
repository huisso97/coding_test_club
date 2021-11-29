import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# print(arr)
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    # arr[i-1][j-1]
    # arr[x-1][y-1]
    res = 0
    for a in range(i,x+1):
        for b in range(j, y+1):
            res += arr[a-1][b-1]
    print(res)