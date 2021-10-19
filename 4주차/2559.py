import sys
sys.stdin = open('2559.txt')

#연속적인 며칠동안의 온도 합이 가장 큰 놈
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# maximum = sum(arr[0:K])

lst = sum(arr[0:K])
maximum = lst
if K == 1:
    print(max(arr))
    exit()
for i in range(N-K):
    lst -= arr[i]
    lst += arr[i+K]
    if lst > maximum:
        maximum = lst
print(maximum)

# 힌트
# 첫구간을 변수에 담아놔
# 반복문 돌릴 때
# 첫번째숫자 빼고 네번째 숫자 더해 그래서 값 비교
