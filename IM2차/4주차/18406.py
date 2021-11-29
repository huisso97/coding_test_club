import sys
sys.stdin = open('18406.txt')

N = list(map(int, input()))

length = len(N)

if sum(N[:length//2]) == sum(N[length//2:]):
    print('LUCKY')
else:
    print('READY')