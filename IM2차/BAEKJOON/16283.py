import sys
sys.stdin = open('16283.txt')


a,b,n,w=map(int, input().split())

result = []
for i in range(1, n+1):
    if i*a + (n-i)*b == w and n-i>0:
        result.append(i)
        result.append(n-i)
if len(result) != 2:
    print(-1)
else:
    print(result[0], result[1])