import sys
sys.stdin = open('2491.txt')

N = int(input())
arr = list(map(int, input().split()))
print(arr)

#모든값들은 현재있는 위치에서 1위 값을 가진다.
asc, des = 1, 1
ans = 1
for i in range(1, N):
    #오름차순인 경우 asc +1
    if arr[i] >= arr[i-1]:
        asc += 1
    #아닌 경우 다시 asc를 1로 시작
    else:
        asc = 1
    if arr[i]<=arr[i-1]:
        des += 1
    else:
        des = 1
    #i값이 달라질때마다 계속해서 최댓값 갱신
    ans = max(ans, asc, des)
print(ans)