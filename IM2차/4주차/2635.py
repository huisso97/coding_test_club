import sys
sys.stdin = open('2635.txt')

num1 = int(input())
arr = [num1]
maximum = 0
second = 0
for i in range(1, num1+1):
    arr.append(i)
    idx = 1
    while True:
        if arr[idx-1]-arr[idx] < 0 :
            if len(arr) > maximum:
                maximum = len(arr)
                second = i
            arr = [num1]
            break
        arr.append(arr[idx-1]-arr[idx])
        idx += 1

arr = [num1, second]
idx = 1
while True:
    if arr[idx-1] - arr[idx] < 0:
        break
    arr.append(arr[idx-1]-arr[idx])
    idx += 1
print(maximum)
print(*arr)