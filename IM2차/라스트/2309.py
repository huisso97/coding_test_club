arr = []

for i in range(9):
    baby = int(input())
    arr.append(baby)
arr.sort()

result = False
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            tmp1 = arr[i]
            tmp2 = arr[j]
            arr.remove(tmp1)
            arr.remove(tmp2)
            result = True
            break
    if result:
        break
for i in arr:
    print(i)
