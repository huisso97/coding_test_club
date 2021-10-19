import sys
sys.stdin = open('5432.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())

    stack = 0
    #쇠막대기..?
    cnt = 0
    for i in range(len(arr)):
        # print(stack)
        if arr[i] == '(':
            stack += 1
        else:
            # tmp = stack.pop()
            stack -= 1
            #레이저?
            if arr[i-1] == '(':
                cnt += stack
            #막대기 끝
            else:
                cnt += 1
    print('#{} {}'.format(tc, cnt))