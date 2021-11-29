import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    res = []
    tmp = [3,6,9]
    for num in range(1, N+1):
        #1자리수
        if num<10:
            if num in tmp:
                res.append('-')
            else:
                res.append(num)
        #2자리수
        elif num<100:
            arr = []
            for val in str(num):
                if int(val) in tmp:
                    arr.append('-')
            if len(arr)==0:
                res.append(num)
            else:
                res.append(''.join(arr))
        # 3자리수
        else:
            arr = []
            for val in str(num):
                if int(val) in tmp:
                    arr.append('-')
            if len(arr) == 0:
                res.append(num)
            else:
                res.append(''.join(arr))
    print(*res)