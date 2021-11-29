import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr1, arr2 = input().split()
    tmp = {'A':1,'B':2,'C':0,'D':1,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':1,'P':1,'Q':1,'R':1,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,}


    lt = 0
    rt = 0
    res = 'SAME'
    while True:
        if len(arr1) != len(arr2):
            res='DIFF'
            break
        if tmp[arr1[lt]] == tmp[arr2[rt]]:
            lt += 1
            rt += 1
        else:
            res = 'DIFF'
            break
        if lt == len(arr1)-1 or rt == len(arr2) -1:
            break
    print('#{} {}'.format(tc, res))
