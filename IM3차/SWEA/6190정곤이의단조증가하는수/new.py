import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            num = arr[i]*arr[j]
            exist = True
            # print(num)
            if num < 10:
                res.append(num)
            else:
                for k in range(len(str(num))-1):
                    if int(str(num)[k+1]) - int(str(num)[k]) >= 0:
                        continue
                    else:
                        exist = False
                        break
                if exist:
                    res.append(num)
    if res:
        print('#{} {}'.format(tc, max(res)))
    else:
        print('#{} {}'.format(tc, -1))
