T = int(input())
for tc in range(1, 1 + T):
    N = int(input())

    corridor = [0] * 201
    for _ in range(N):
        x, y = map(int, input().split())
        if x <= y:
            start = (x + 1) // 2
            end = (y + 1) // 2
        else:
            start = (y + 1) // 2
            end = (x + 1) // 2
        for j in range(start, end + 1):
            corridor[j] += 1

    result = max(corridor)
    print('#{}'.format(tc), result)