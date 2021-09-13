import sys
sys.stdin = open('14696.txt')


N = int(input())
# 총 게임 횟수 N번을 실행한다.

for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    A = a[1:]
    B = b[1:]
    if A.count(4) > B.count(4):
        print('A')
    elif A.count(4) < B.count(4):
        print('B')
    else:
        if A.count(3) > B.count(3):
            print('A')
        elif A.count(3) < B.count(3):
            print('B')
        else:
            if A.count(2) > B.count(2):
                print('A')
            elif A.count(2) < B.count(2):
                print('B')
            else:
                if A.count(1) > B.count(1):
                    print('A')
                elif A.count(1) < B.count(1):
                    print('B')
                else:
                    print('D')

