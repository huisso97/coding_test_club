import sys
sys.stdin = open('2491.txt')

N = int(input())

arr = list(map(int, input().split()))

while True:
    cnt = 0
    maximum = 0
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            cnt += 1
        else:
            cnt += 1
            if maximum < cnt:
                maximum = cnt
            cnt = 0
    for i in range(1, len(arr)):
        if arr[-i] <= arr[-i-1]:
            cnt += 1
        else:
            cnt += 1
            if maximum < cnt:
                maximum = cnt
            cnt = 0
    break
if maximum >= 3:
    print(maximum)
else:
    print(2)

