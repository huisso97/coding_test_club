import sys
sys.stdin = open('1244.txt')

N = int(input())
arr = [0]+list(map(int, input().split()))
M = int(input())

for k in range(M):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(len(arr)):
            if i%num == 0:
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
    elif sex == 2:
        idx = 0
        while True:
            if 0< num-idx and num+idx<len(arr) and arr[num-idx] == arr[num+idx]:
                if arr[num-idx] == 0:
                    arr[num-idx] = 1
                    arr[num+idx] = 1
                else:
                    arr[num-idx] = 0
                    arr[num+idx] = 0
                idx += 1
            else:
                break
arr.pop(0)
while arr:
    if len(arr)<=20:
        print(*arr)
        break
    else:
        print(*arr[:20])
        del arr[:20]