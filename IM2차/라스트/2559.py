N, K = map(int, input().split())
arr = list(map(int, input().split()))

lst = sum(arr[0:K])
maximum = lst
if K == 1:
    print(max(arr))
else:
    for i in range(N-K):
        lst -= arr[i]
        lst += arr[i+K]
        if lst > maximum:
            maximum = lst

    print(maximum)