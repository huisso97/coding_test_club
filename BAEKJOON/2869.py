A, B, V = map(int, input().split())
day = A-B
cnt = 0
while True:
    # if V0:
    #     break
    V -= A
    if V <= 0:
        cnt += 1
        break
    V += B
    cnt += 1
    # print(V)
    # print(cnt)
print(cnt)