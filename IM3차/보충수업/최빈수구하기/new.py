import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    tc = int(input())
    num_list = list(map(int, input().split()))
    # num_list.sort()
    res = [0]*101
    # print(res)
    for i in range(len(num_list)):
        res[num_list[i]] += 1
    maximum = max(res)
    for i in range(len(res)-1, -1, -1):
        if res[i] == maximum:
            print('#{} {}'.format(tc, i))
            break