import sys
sys.stdin = open('2578.txt')

board = [list(map(int, input().split())) for _ in range(5)]
arr = []
for i in range(5):
    numbers = list(map(int, input().split()))
    arr += numbers
print(arr)
bingo = 0
#행
result1 = [0]*5
#열
result2 = [0]*5
#정대각선
result3 = [0]
#역대각선
result4 = [0]
#사회자가 수를 부르는 횟수
cnt = 0
while bingo != 3:
    for i in range(5):
        for j in range(5):
            if numbers[cnt] == board[i][j]:
                result1[i] += 1
                result2[j] += 1
                if i == j:
                    result3[0] += 1
                if i == 4-j:
                    result4[0] += 1
            if result1.count(5) + result2.count(5) + result3.count(5) + result4.count(5) >=3:
                bingo = 3
            cnt += 1
print(cnt)