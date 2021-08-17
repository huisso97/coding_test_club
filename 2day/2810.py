
N = int(input())
seat = input()
l = 0
for i in range(N-1):
    if seat[i] == 'L':
        l += 1
result = N+1 - l//2
print(result)

