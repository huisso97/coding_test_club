import sys
sys.stdin = open('in1.txt')
# sys.stdin = open('in2.txt')
# sys.stdin = open('in3.txt')
# sys.stdin = open('in4.txt')
# sys.stdin = open('in5.txt')

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
lt = 0
rt = n-1
while lt <= rt:
    mid = (rt+lt)//2
    if m == arr[mid]:
        print(mid)
        break
    if m > arr[mid]:
        # print(arr[mid])
        lt += 1
    else: # m < mid
        # print(arr[mid])
        rt -= 1

