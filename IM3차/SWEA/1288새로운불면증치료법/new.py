import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0]*10
    k = 1
    while 0 in arr:
        # print(arr)
        # print(N)
        num = str(N*k)
        for val in num:
            # print(val)
            arr[int(val)] += 1
        if 0 not in arr:
            break
        k += 1

    print('#{} {}'.format(tc, k*N))
