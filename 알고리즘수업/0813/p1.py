import sys
sys.stdin = open('p1.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    print(arr[::-1])