import sys
sys.stdin = open('1712.txt')

a, b, c = map(int, input().split())
if b >= c: #A+B*n = C*n 일 때, 수입 비용 같아지기 때문에, b>=c일 경우 손익분기점 나타나지 않음 =>걸러
    print(-1)
else:
    print(int(a / ( c - b ) + 1))