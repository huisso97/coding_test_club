import sys
sys.stdin = open('10157.txt')

#결과물: (열+1, 행+1)

x, y = map(int, input().split())
K = int(input())

arr = [[0]*x for _ in range(y)]

#열
dx = [0, 1, 0, -1]
#행
dy = [1, 0, -1, 0]

arr[0][0] = 1
idx = 2
i = 0
j = 0
k = 0

while idx<=x*y:
    #인덱스 값
    nx = j+dx[k]
    ny = i+dy[k]

    if 0<=nx<x and 0<=ny<y and arr[ny][nx] == 0:
        arr[ny][nx] = idx
        idx += 1
        i = ny
        j = nx
    else:
        k = (k+1) % 4
    if idx == K+1:
        print(nx + 1, ny + 1)

        break

else:
    print(0)
