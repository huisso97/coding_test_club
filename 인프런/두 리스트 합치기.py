import sys
sys.stdin = open('in1.txt')
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1=p2=0
result = []
# print(m)
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        result.append(a[p1])
        p1+=1
    else:
        result.append(b[p2])
        p2+=1
if p1 < n:
    result += a[p1:]
else:
    result += b[p2:]
print(result)