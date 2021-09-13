import sys
sys.stdin = open('2563.txt')

paper = [[0]*101 for _ in range(101)]

N = int(input())
result = 0
for _ in range(N):
    start = list(map(int, input().split()))

    for i in range(10):
        for j in range(10):
            if paper[start[1]+i][start[0]+j] == 0:
                paper[start[1]+i][start[0]+j] = 1
                result +=1
print(result)