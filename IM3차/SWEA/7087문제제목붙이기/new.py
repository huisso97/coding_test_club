import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(input()[0])
    arr.sort()
    cnt = 0
    print(arr)
    for i in range(len(arr)-1):
        if ord(arr[i+1])-ord(arr[i]) <= 1:
            cnt += 1
            continue
        else:
           break
    print(cnt)