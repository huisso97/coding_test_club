import sys
# sys.stdin = open('in1.txt')
# sys.stdin = open('in2.txt')
# sys.stdin = open('in3.txt')
# sys.stdin = open('in4.txt')
sys.stdin = open('in5.txt')

arr = [list(map(int, input().split())) for _ in range(7)]

# zip으로 행을 열로 돌려서 확인

for row in zip(*arr):
    arr.append(list(row))

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])-5+1):
        tmp = arr[i][j:j+5]
        # print(tmp)
        if tmp == tmp[::-1]:
            print(tmp)
            cnt += 1
print(cnt)