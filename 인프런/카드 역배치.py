import sys
sys.stdin = open('in1.txt')


arr = [i for i in range(21)]
for i in range(10):
    s, e = map(int, input().split())
    for j in range((e-s)//2+1):
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
print(arr)