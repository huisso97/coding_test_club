import sys
sys.stdin = open('10158.txt')

w, h = map(int,input().split())
p, q = map(int, input().split())
t = int(input())

while t!=0:
    p += 1
    q += 1
    t -= 1
    if p > w:
        if q > h:
            while p != 0 and q != 0:
                t -= 1
                p -= 1
                q -= 1
        if q < 0:
            while p != 0 and q != h:
                t -= 1
                p -= 1
                q += 1
    if p < 0:
        if q > h:
            while p != w and q != 0:
                t -= 1
                p += 1
                q -= 1
        if q < 0:
            while p != w and q != h:
                t -= 1
                p += 1
                q += 1
print(p,q)