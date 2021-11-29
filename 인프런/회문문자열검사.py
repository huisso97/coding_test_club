import sys
sys.stdin = open('in1.txt')



n = int(input())
for i in range(1, n+1):
    arr = input().upper()
    if arr == arr[::-1]:
        print('#{} YES'.format(i))
    else:
        print('#{} NO'.format(i))