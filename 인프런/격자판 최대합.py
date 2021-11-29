import sys
sys.stdin = open('in1.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

maximum = 0

for i in range(n):
    sum1 = sum2 = sum3 = sum4 = 0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
        sum3 += arr[j][j]
        sum4 += arr[j][n-j-1]
    if sum1 > maximum:
        maximum = sum1
    if sum2 > maximum:
        maximum = sum2
    if sum3 > maximum:
        maximum = sum3
    if sum4 > maximum:
        maximum = sum4
    # sum1 = 0
    # sum2 = 0
print(maximum)
