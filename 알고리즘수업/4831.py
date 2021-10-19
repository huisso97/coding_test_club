import sys
sys.stdin = open('4831.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    bus_stop = [False]*(N+1)
    for i in range(len(station)):
        bus_stop[station[i]] = True
    pre = 0
    new = K
    ans = 0
    while True:
        if new >=N:
            break
        if bus_stop[new]:
            ans += 1
            pre = new
            new += K
        else:
            new -= 1
            if new == pre:
                ans = 0
                break
    print('#{} {}'.format(tc, ans))
