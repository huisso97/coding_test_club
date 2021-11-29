import sys
sys.stdin = open('5174.txt')

def recur(cur): #dfs
    pass

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    #부모, 자식, 부모, 자식

