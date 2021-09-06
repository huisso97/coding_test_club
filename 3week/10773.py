K = int(input())
arr = [0]
for i in range(K):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        arr.pop()
print(sum(arr))

