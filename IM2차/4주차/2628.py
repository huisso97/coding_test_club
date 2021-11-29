import sys
sys.stdin = open('2628.txt')

x, y = map(int, input().split())

N = int(input())
line_x = [0, x]
line_y = [0, y]
for i in range(N):
    a, b = map(int, input().split())
    if a == 0:
        line_y.append(b)
    else:
        line_x.append(b)
line_x.sort()
line_y.sort()
maximum = 0
tmp = 0
for m in range(len(line_y)-1):
    h = line_y[m+1] - line_y[m]
    for n in range(len(line_x)-1):
        w = line_x[n+1] - line_x[n]
        tmp = h*w
        if maximum < tmp:
            maximum = tmp
print(maximum)