board = [list(map(int, input().split())) for _ in range(5)]
mic = [list(map(int, input().split())) for _ in range(5)]

number = []
for i in range(len(mic)):
    for j in range(len(mic)):
        number.append(mic[i][j])

column = [0]*5
row = [0]*5
line1 = [0]
line2 = [0]

cnt = 0
exist = False
# for k in ran/ge(len(number)):
while True:
    for i in range(5):
        for j in range(5):
            if number[cnt] == board[i][j]:
                column[j] += 1
                row[i] += 1
                if i==j:
                    line1[0] += 1
                if i==4-j:
                    line2[0] += 1
                exist = True
                break
        if exist:
            exist=False
            break
    cnt += 1
    if column.count(5) + row.count(5) + line1.count(5) + line2.count(5) >= 3:
        break
print(cnt)
