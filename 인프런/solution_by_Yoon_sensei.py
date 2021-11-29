# 1
n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]

# print(apple)
result = 0
for i in range(n//2+1):
    result += sum(apple[i][n//2-i:n//2+i])
for i in range(n//2+1, n):
    for j in range(n)
