import sys
sys.stdin = open('2166.txt')
N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]

for num in range(1, N+1):
    x, y, xsize, ysize = map(int, input().split())
    for x_idx, X in enumerate(arr):
        for y_idx, Y in enumerate(X):
            if x<=x_idx<= xsize-1 and y<=y_idx<=ysize-1:
                arr[x_idx][y_idx] = num
