import sys
sys.stdin = open('10163.txt')
#행이 뒤집어져있다
N = int(input())
paper = [list( 0 for _ in range(1001)) for _ in range(1001)]

for i in range(1, N+1):
    x, y, width, height = map(int, input().split())
    for a in range(x, x+width):
        for b in range(y, y+height):
            paper[a][b] = i

for k in range(1, N+1):
    cnt = 0
    for i in range(len(paper)):
        for j in range(len(paper)):
            if paper[i][j] == k:
                cnt += 1
    print(cnt)

