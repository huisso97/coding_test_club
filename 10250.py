# 열이 작을수록
    # 행이 작을수록
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    # print(H, W, N)
    arr = [[0 for _ in range(W)] for _ in range(H)]

    i = 1
    exist = False
    result = ''
    for k in range(W):
        for j in range(H):
            arr[j][k] = i
            if i == N:
                height = j+1
                width = k+1
                if width < 10:
                    result = str(height)+'0'+str(width)
                else:
                    result = str(height)+str(width)
                print(result)
                exist = True
                break
            i+=1
        if exist:
            break

    # print(arr)