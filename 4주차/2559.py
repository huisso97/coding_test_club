import sys
sys.stdin = open('2559.txt')

#연속적인 며칠동안의 온도 합이 가장 큰 놈
N, K = map(int, input().split())
arr = list(map(int, input().split()))

maximum = -111*N

for i in range(len(arr)-K):
    summation = sum(arr[i:i+K])
    if summation > maximum:
        maximum = summation
print(maximum)
