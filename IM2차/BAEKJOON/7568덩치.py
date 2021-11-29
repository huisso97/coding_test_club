# import sys
# sys.stdin = open('input.txt')
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
# print(students)
# 기준 옮겨줄 for문
res = [1]*N
for i in range(N):
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1]<arr[j][1]:
            res[i] += 1
print(res)
# max_x = 0
# max_y = 0
# for i in range(N):
#     if students[i][0] > max_x and students[i][1] > max_y:
#         max_x = students[i][0]
#         max_y = students[i][1]
# cnt = 1
# res = []
#
# for i in range(N):
#     if students[i][0]<max_x and students[i][0]<max_y:
#         cnt += 1
#         res.append(cnt)
#         max_x = students[i][0]
#         max_y = students[i][1]
#     elif students[i][0]==max_x and students[i][0]==max_y:
#         res.append(1)
#     elif students[i][0]<max_x and students[i][0]>max_y or students[i][0]>max_x and students[i][0]<max_y:
#         res.append(cnt)
# print(res)