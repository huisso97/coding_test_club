import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    exist = False
    for i in range(len(arr)-2):
        if arr[i]-arr[i+1] == arr[i+1]-arr[i+2]:
            exist = True
            continue
        else:
            exist = False
            break
    if exist:
        for j in range(len(arr)-1):
            if arr[j] - arr[j+1] > 0:
                print('descending')
                break
            else:
                print('ascending')
                break
    else:
        print('mixed')
