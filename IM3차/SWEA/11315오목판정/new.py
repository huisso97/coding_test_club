import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # ans = False
    for i in range(N):
        ans = True
        for j in range(N):
            if arr[i][j] == 'o':
                continue
            else:
                ans = False
                break
        if ans:
            print('YES')
            break
        else:
            pass
    for i in range(N):
        ans = True
        for j in range(N):
            if arr[j][i] == 'o':
                continue
            else:
                ans = False
                break
        if ans:
            print('YES')
            break
        else:
            pass
    for i in range(N):
        ans = True
        for j in range(N):
            if arr[j][j] == 'o':
                continue
            else:
                ans = False
                break
        if ans:
            print('YES')
            break
        else:
            pass