import sys
sys.stdin = open('신한2.txt')


#규칙이 dp[n] = dp[n-3]+dp[n-2]+dp[n-1] 인가
dp = [0 for _ in range(100)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
def Find(n):
    if dp[n]:
        return dp[n]
    dp[n] = Find(n-3)+Find(n-2)+Find(n-1)
    return dp[n]


T = int(input())

for tc in range(1, T+1):
     number = int(input())
     print(Find(number))