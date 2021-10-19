T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    lst = []
    exist = False
    for i in range(N//2+1):
        for j in range(N//2-i, N//2+i+1):
            if i == N-i-1:
                lst.append(farm[i][j])
                exist = True
            if exist == False:
                lst.append(farm[i][j])
                lst.append(farm[N-i-1][j])
    print(lst)
    result = 0
    for i in range(len(lst)):
        result += int(lst[i])
    print('#{} {}'.format(tc, result))

'''
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    result = 0
    # 늘어날 때
    for i in range(n//2+1):
        result += sum(farm[i][n//2-i:n//2+1+i])
        print(farm[i][n//2-i : n//2+1+i])
    # 줄어들 때
    for i in range(n//2-1, -1, -1):
        result += sum(farm[n-i-1][n//2-i:n//2+1+i])
        print(farm[n-i-1][n//2-i:n//2+1+i])

    print('#{} {}'.format(tc, result))
'''