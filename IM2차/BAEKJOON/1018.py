N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N-8):
    for j in range(M-8):
       if arr[i][j] == 'W':
           for m in range(8):
               for n in range(8):

       else: