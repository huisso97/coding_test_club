import sys
sys.stdin = open('in1.txt')
# sys.stdin = open('in2.txt')
# sys.stdin = open('in3.txt')
# sys.stdin = open('in4.txt')
# sys.stdin = open('in5.txt')

def Count(mid):
    global arr
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i] // mid
    return cnt
k, n = map(int, input().split())
arr = []

for _ in range(k):
    arr.append(int(input()))
arr.sort()
lt = 1
rt = arr[-1]
result = 0
while True:
    if lt == rt:
        break
    # mid는 길이
    mid = (lt+rt)//2
    if Count(mid) >= n:
        result = Count(mid)
        print(Count(mid))
        lt += 1
    else:
        rt -= 1