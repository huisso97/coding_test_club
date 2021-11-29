import sys
# sys.stdin = open('in1.txt')
# sys.stdin = open('in2.txt')
# sys.stdin = open('in3.txt')
# sys.stdin = open('in4.txt')
sys.stdin = open('in5.txt')
n = int(input())
result = []
for i in range(n):
    arr = list(map(int, input().split()))
    result.append(arr)
print(result)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for y in range(n):
    for x in range(n):
        exist = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # print(nx)
            if 0<=nx<n and 0<=ny<n:
                if result[ny][nx] < result[y][x]:
                    # print(result[y][x], result[ny][nx])
                    continue
                else:
                    exist = False
                    break
        if exist:
            cnt += 1
print(cnt)