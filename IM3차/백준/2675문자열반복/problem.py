import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    cnt, arr = input().split()
    cnt = int(cnt)
    for i in range(len(arr)):
        for j in range(cnt):
            print(arr[i], end='')
    print()