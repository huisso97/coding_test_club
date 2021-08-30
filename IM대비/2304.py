import sys
sys.stdin = open('2304.txt')
#기둥의 숫자
N = int(input())
maxValue = -1
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
data = sorted(data)
for i in range(N):
    if data[i][i] >= maxValue:
        maxValue = data[i][1]
        max_idx = i
result = maxValue
s = 0
for m in range(1, max_idx+1): #left
    if data[m][1] <= data[m][1]:
        result += data












