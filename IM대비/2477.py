n = int(input())

lines = []

for _ in range(6):
    lines.append(list(map(int, input().split())))

total_idx = [1,2,3,4]

exist = 0
for i in range(6):
    for j in range(i+1, 6):
        if lines[i][0] == lines[j][0]:
            # for k in range(1, 5):
            #     if k != lines[j][0] and k != lines[j-1][0]:
            #         total_idx.append(k)
            total_idx.remove(lines[i][0])
            exist += 1
            break
    if exist == 2:
        break

#작은 범위의 방향 나타내는 인덱스
idx = []

total_area = []
for i in range(len(lines)):
    if lines[i][0] == total_idx[0] or lines[i][0] == total_idx[1]:
        total_area.append(lines[i][1])
        #4랑 2가 담겨진 인덱스
        idx.append((i+3)%6)

total = total_area[0]*total_area[1]
small = lines[idx[0]][1]*lines[idx[1]][1]

print((total-small)*n)