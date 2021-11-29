import sys
sys.stdin = open('in1.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    row, way, cnt = map(int, input().split())
    if way == 0:
        for j in range(cnt):
            tmp = arr[row-1].pop(0)
            arr[row-1].append(tmp)
    else:
        for j in range(cnt):
            tmp = arr[row-1].pop()
            arr[row-1].insert(0, tmp)
print(arr)
s=0
e=n-1
result = 0
for i in range(n):
    if i < n// 2 :
        for j in range(s, e+1):
            result += arr[i][j]
        s += 1
        e -= 1
    else:
        for j in range(s, e+1):
            result += arr[i][j]
        s -= 1
        e += 1
print(result)