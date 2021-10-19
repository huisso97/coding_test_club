import sys
sys.stdin = open('1210.txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = 0

    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    while y != 0:
        #오른쪽
        if 0<=x+1<100 and ladder[y][x+1]:
            ladder[y][x + 1] = 0
            x+=1

        #왼쪽
        elif 0<=x-1<100 and ladder[y][x-1]:
            ladder[y][x - 1] = 0
            x-=1
        #위
        elif 0<=y-1<100 and ladder[y-1][x]:
            ladder[y-1][x] = 0
            y-=1
    print('#{} {}'.format(tc, x))