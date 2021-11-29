N = int(input())
exist = False
for num in range(1, N):
    tmp = str(num)
    res = num
    # print(res)
    # print(type(res))
    for i in range(len(tmp)):
        res += int(tmp[i])
        # print(res)
    if res == N:
        print(num)
        exist = True
        break
if exist == False:
    print(0)