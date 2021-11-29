import sys
sys.stdin = open('2578.txt')

# def Bingo():
#     global lst, bingo, cnt, col, row, diag_2, diag_1
#     cnt += 1
#
#     if visited[0][0] + visited[1][1] + visited[2][2] + visited[3][3] + visited[4][4] == 5:
#         diag_1 = 1
#     if visited[4][0] + visited[3][1] + visited[2][2] + visited[1][3] + visited[0][4] == 5:
#         diag_2 = 1
#     for i in range(len(board)):
#         k = visited[i][:5]
#         if k not in lst:
#             if sum(k) == 5:
#                 lst.append(k)
#                 col += 1
#         for j in range(len(board)):
#
#             if sum(visited[:5][i]) == 5:
#                 row = 1
#
#
# board = [list(map(int, input().split())) for _ in range(5)]
# mc = [list(map(int, input().split())) for _ in range(5)]
# visited = [list(0 for _ in range(5)) for _ in range(5)]
# number = []
# for i in range(5):
#     for j in range(5):
#         number.append(mc[i][j])
#
# col = 0
# row = 0
# diag_1 = 0
# diag_2 = 0
# cnt = 0
# bingo = 0
# lst = []
# for num in number:
#     for i in range(len(board)):
#         exist = False
#         for j in range(len(board)):
#             if board[i][j] == num:
#                 visited[i][j] = 1
#                 Bingo()
#                 if col + row + diag_1 + diag_2 >= 3:
#                     print(cnt)
#                     exit()
#                 exist = True
#                 break
#         if exist:
#             break
#
# board = [list(map(int, input().split())) for _ in range(5)]
# arr = []
# for i in range(5):
#     numbers = list(map(int, input().split()))
#     arr += numbers
#
# bingo = 0
# #행
# result1 = [0]*5
# #열
# result2 = [0]*5
# #정대각선
# result3 = [0]
# #역대각선
# result4 = [0]
# #사회자가 수를 부르는 횟수
# cnt = 0
# sub = False
# while True:
#     for i in range(5):
#         for j in range(5):
#             if arr[cnt] == board[i][j]:
#                 result1[i] += 1
#                 result2[j] += 1
#                 if i == j:
#                     result3[0] += 1
#                 if i == 4-j:
#                     result4[0] += 1
#                 sub = True
#                 break
#         #이중 포문 나오기 위한 임시 변수
#         if sub:
#             sub = False
#             break
#     cnt += 1
#     if result1.count(5) + result2.count(5) + result3.count(5) + result4.count(5) >=3:
#         break
# print(cnt)



bingo = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]
read = []
for i in range(len(arr)):
    for j in range(len(arr)):
        read.append(arr[i][j])
# print(read)

result1 = [0]*5
result2 = [0]*5
result3 = [0]
result4 = [0]

cnt = 0

exist = False
while True:
    for i in range(5):
        for j in range(5):
            if read[cnt] == bingo[i][j]:
                result1[i] += 1
                result2[j] += 1
                if i == j:
                    result3[0] += 1
                if i == 4-j:
                    result4[0] += 1
                exist = True
                break
        if exist:
            exist = False
            break
    cnt += 1
    if result1.count(5) + result2.count(5) +result3.count(5) + result4.count(5)>=3:
        break
print(cnt)































