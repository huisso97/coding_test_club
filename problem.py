import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr=list(map(int, input().split()))
    n = arr[0]
    score = arr[1:]
    pyeongun = sum(score) / n
    cnt = 0
    # print(pyeongun)
    for i in score:
        # print(i)
        if i > pyeongun:
            cnt += 1
    result = cnt / n * 100
    print(f'{result:.3f}%')

# 관이꺼 = 최소희
T = int(input())
for tc in range(1, T+1):
    arr=list(map(int, input().split()))
    n = arr[0]
    score = arr[1:]
    pyeongun = sum(score) / n
    cnt = 0
    # print(pyeongun)
    for i in score:
        # print(i)
        if i > pyeongun:
            cnt += 1
    result = round(cnt / n * 100, 3)
    result_str = list(str(result))
    # print(result_str)
    if result_str[-1] == '0':
        for i in range(2):
            result_str.append('0')
    result_str.append('%')
    print(''.join(result_str))