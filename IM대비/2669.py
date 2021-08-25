arr = [[0]*101 for _ in range(101)]
for _ in range(4):
    r1, c1, r2, c2 = map(int, input().split())
    #x좌표 범위 주의!!
    for i in range(r1, r2):
        #y좌표
        for j in range(c1, c2):
            if arr[i][j] == 0:
                arr[i][j] = 1
result = 0
for i in arr:
    result += sum(i)
print(result)