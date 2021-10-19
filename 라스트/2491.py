N = int(input())
arr = list(map(int, input().split()))

cnt1 = 1
maximum = 0
cnt2 = 1
result1 = []
result2 = []
minimum = max(arr)
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        cnt1 +=1
    else:
        result1.append(cnt1)
        cnt1 = 1
result1.append(cnt1)
for i in range(len(arr) - 1):
    if arr[i]>=arr[i+1]:
        cnt2 += 1
    else:
        result2.append(cnt2)
        cnt2 = 1
result2.append(cnt2)
print(max(max(result1), max(result2)))

