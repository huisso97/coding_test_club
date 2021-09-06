N = int(input())
num = int(input())

connected = list(list(map(int, input().split())) for _ in range(num))
arr = [[0]*N for _ in range(N)]
for i in range(1, num+1):
    arr[connected[i][0]] = connected[i][1]
print(arr)
