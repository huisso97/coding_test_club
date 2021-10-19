N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
boat = []
s = 0
e = len(arr)-1
cnt = 0
while s <= e:
    if arr[s]+arr[e] <= M:
        cnt += 1
        s += 1
        e -= 1
    else:
        cnt += 1
        e -=1
print(cnt)