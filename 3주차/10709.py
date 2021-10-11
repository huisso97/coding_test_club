import sys
sys.stdin = open('10709.txt')

h, w = map(int, input().split())


sky = list(list(input()) for _ in range(h))
result = list([0]*w for i in range(h))

for i in range(h):
    meet = False
    num = 0
    for j in range(w):
        if sky[i][j] == 'c':
            result[i][j] = 0
            meet = True
            num = 0
        else:
            #c를 만나기 전
            if meet == False and sky[i][j] == '.':
                result[i][j] = -1
            #c를 만난 후
            elif meet == True and sky[i][j] == '.':
                num += 1
                result[i][j] = num
for i in range(h):
    for j in range(w):
        print(result[i][j], end=' ')
    print()