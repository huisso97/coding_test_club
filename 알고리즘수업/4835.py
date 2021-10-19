import sys
sys.stdin = open('4835.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    number = list(map(int, input().split()))
    maximum = 0
    minimum = 10001*M
    for i in range(len(number)-M+1):
        if sum(number[i:i+M]) > maximum:
            maximum = sum(number[i:i+M])
        if sum(number[i:i+M]) < minimum:
            minimum = sum(number[i:i+M])
    print('#{} {}'.format(tc, maximum-minimum))
