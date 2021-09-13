import sys
sys.stdin = open('10163.txt')

n = int(input())

arr = [[-1]*1001 for _ in range(1001)]

for idx in range(n):
    square = list(map(int, input().split()))
    #행 높이
    for i in range(square[3]):
        #열 너비
        for j in range(square[2]):
            #자기 영역에 자신의 인덱스 값 넣어줌
            arr[square[1]+i][square[0]+j] = idx
for idx in range(n):
    result = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == idx:
                result +=1
    print(result)