import sys
sys.stdin = open('13413.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    origin = list(input())
    goal = list(input())
    cnt = 0
    for i in range(N-1):
        if origin[i] != goal[i]:
            for j in range(i+1, N):
                if origin[j] != goal[j] and origin[i]!=origin[j]:
                    origin[i], origin[j] = origin[j], origin[i]
                    cnt += 1
    for i in range(N):
        if origin[i] != goal[i]:
            cnt +=1
            if origin[i] == 'W':
                origin[i] = 'B'
            else:
                origin[i] = 'W'

    print(origin)
    print(goal)

