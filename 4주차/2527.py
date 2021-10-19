import sys
sys.stdin = open('2527.txt')

for i in range(4):
    paper = [[0 for _ in range(50001)] for _ in range(50001)]
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    for k in range(y1, q1+1):
        for j in range(x1, p1+1):
            paper[k][j] += 1

    for k in range(y2, q2+1):
        for j in range(x2, p2+1):
            paper[k][j] += 1

    h = 0
    for k in range(len(paper)):
        w = 0
        for j in range(len(paper)):
            if paper[k][j] == 2:
                w += 1
        if w == 1:
            print('c')
        elif w > 1:
            print('b')
        elif w == 0:
            print('d')
        h += 1
    if h > 0 and w > 0:
        print('a')

# for i in range(4):
#     x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
#
#     if (p1 > x2 and q1 > y2) or (p2 > x1 and q2 > y1):
#         print('a')
#     elif (p1 == x2) or (x1 == p2):
#         print('b')
#     elif (x1 == p2 and y1 == p2) or (p1 == x2 and q1 == y2):
#         print('c')
#     else:
#         print('d')