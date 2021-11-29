import sys
sys.stdin = open('2167.txt')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
def Summation(i,j,x,y):
    summation = 0
    for a in range(i, x + 1):
        sub = 0
        for b in range(j, y + 1):
            sub += arr[a - 1][b - 1]
        summation += sub
    return summation
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(Summation(i,j,x,y))