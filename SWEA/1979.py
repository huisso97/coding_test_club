import sys
sys.stdin = open('1979.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))
    result = 0
    cnt = 0
    #가로 체크
    for x in range(n):
        for y in range(n):
            if arr[x][y] == 1:
                cnt += 1
            if arr[x][y] == 0 or y == n-1: #0을 만났거나, 벽을 만났을 때
                if cnt == k: #이전에 계산한 카운트가 k라면 result에 카운트
                    result += 1
                cnt = 0 # 카운트 초기화

    for y in range(n):
        #열(y)기준으로 보기
        for x in range(n):
            if arr[x][y] == 1: #1이면 카운트
                cnt += 1
            if arr[x][y] == 0 or x == n-1 :  # 0을 만났거나 벽을 만났을 때
                if cnt == k:   # 이전에 계산한 카운트가 k라면 result에 카운트
                    result += 1
                cnt = 0
    print(result)