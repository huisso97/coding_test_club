import sys
sys.stdin = open('신한3.txt')



n= int(input())

arr= list(map(int, input().split()))
result = []
for i in range(n):
    if arr[i] in result:
        pass
    else:
        result.append(arr[i])

for i in sorted(result):
    print(i, end=' ')
# print(sorted(result))