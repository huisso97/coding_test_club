E,S,M = map(int, input().split())

e, s, m = 0, 0, 0

cnt = 0
while True:
    if e == E and s == S and m == M:
        print(cnt)
        break
    e += 1
    s += 1
    m += 1
    cnt += 1

    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

