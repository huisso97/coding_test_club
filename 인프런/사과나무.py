import sys
sys.stdin = open('in1.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
s = e = n//2
for i in range(n):
    if i < n//2:
        for j in range(s, e+1):
            result += arr[i][j]
        s -= 1
        e += 1
    else:
        for j in range(s, e+1):
            result += arr[i][j]
        s += 1
        e -= 1
print(result)