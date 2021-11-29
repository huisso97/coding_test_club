import sys
# sys.stdin = open('in1.txt')
# sys.stdin = open('in2.txt')
# sys.stdin = open('in3.txt')
# sys.stdin = open('in4.txt')
sys.stdin = open('in5.txt')

arr = [list(map(int, input().split())) for _ in range(9)]
# 행
# 열

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exist = True
for i in range(9):
    row_list = []
    column_list = []
    for j in range(9):
        column_list.append(arr[i][j])
        row_list.append(arr[j][i])
    row_list.sort()
    column_list.sort()
    if row_list != num_list:
        exist = False
    if column_list != num_list:
        exist = False

# 3*3
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        three_list = []
        three_list += arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
        three_list.sort()
        # print(three_list)
        if three_list != num_list:
            exist = False
    three_list = []
if exist:
    print('YES')
else:
    print('NO')