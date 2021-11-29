import sys
sys.stdin = open('13413.txt')

########1#############
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 지금 있는 오셀로
    origin = list(input())
    # 목표로 하는 오셀로
    target = list(input())
    # print(origin)
    cnt = 0
    # 위치를 바꿔주는 부분
    for i in range(n):
        if origin[i] != target[i]:
            # print(i)
            # print(origin[i], target[i])
            for j in range(i+1, n):
                if origin[j] != target[j] and origin[i] != origin[j]:
                    print(origin)
                    origin[i], origin[j] = origin[j], origin[i]
                    print(origin)
                    cnt += 1
                    break

    # 색깔을 바꿔주는 부분
    for i in range(n):
        if origin[i] != target[i]:
            # print(origin)
            if origin[i] == 'W':
                origin[i] = 'B'
                print(origin)
            else:
                origin[i] = 'W'
                print(origin)
            cnt += 1
    print(cnt)


########2#############
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    origin = list(input())
    target = list(input())
    cnt = 0

    # 접근 방법 두가지
    # 색먼저 바꾸기 or 자리먼저 바꾸기
    # 색을 먼저 바꾸려면 우선 origin과 target이 가지고 있는 색깔 수가 같을 때 까지 바꿔주고
    # 그 이후에 자리 바꾸기로 접근해도 되고
    # 자리바꾸기를 먼저 해주고 색깔 바꾸기도 가능하다.
    w = target.count('W')
    b = target.count('B')
    for i in range(n):
        if origin[i] != target[i]:
            # print(origin)
            if origin[i] == 'W':
                origin[i] = 'B'
                # print(origin)
            else:
                origin[i] = 'W'
                # print(origin)
            cnt += 1
        if origin.count('W') == w and origin.count('B') == b or origin == target:
            break
    s = 0
    e = 0
    while True:
        if e >= n-1 or origin == target:
            break
        if origin[s] == target[s]:
            s += 1
            e += 1
        else:
            e += 1
            if origin[e] != target[e] and origin[s] != origin[e]:
                origin[s], origin[e] = origin[e], origin[s]
                cnt += 1
                s = e

    print(cnt)