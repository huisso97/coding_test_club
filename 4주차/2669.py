import sys
sys.stdin = open('2669.txt')

square = [[0]*100 for _ in range(100)]
arr = []
#x는 열 y는 행
for i in range(4):
    arr.append(list(map(int, input().split())))
for i in range(len(arr)):
    left_x = arr[i][0]
    left_y = arr[i][1]
    right_x = arr[i][2]
    right_y = arr[i][3]
    for j in range(left_y, right_y):
        for k in range(left_x, right_x):
            square[j][k] = 1
ans = 0
for i in range(len(square)):
    for j in range(len(square)):
       if square[i][j] == 1:
           ans += 1
print(ans)