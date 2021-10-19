import sys
sys.stdin = open('5356.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)
    result = []
    for i in range(max_len):
        for j in range(len(arr)):
            try:
                result.append(arr[j][i])
                # print(result)
            except:
                pass
    print('#{}'.format(tc), end=' ')
    for i in range(len(result)):
        print(result[i], end='')
    print()
'''
꽌
T = int(input())

for tc in range(1, T+1):
    word = [input() for _ in range(5)]
    max_len = 0
    result = ''
    for i in range(len(word)):
        if max_len < len(word[i]):
            max_len = len(word[i])

    for i in range(max_len):
        tmp = ''
        for j in range(5):
            if i >= len(word[j]):
                continue
            if word[j][i]:
                tmp += word[j][i]
        result += tmp
    print('#{} {}'.format(tc, result))
'''