import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))

    cnt = 0

    while True:
        if sum(arr) == 0:
            break
        for i in range(len(arr)):
            if arr[i] == 1:
                # arr[i:] = 0
                for j in range(i, len(arr)):
                    if arr[j] == 0:
                        arr[j] = 1
                    else:
                        arr[j] = 0
                cnt += 1
    print('#{} {}'.format(tc, cnt))