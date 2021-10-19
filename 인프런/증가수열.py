N = int(input())
arr = list(map(int, input().split()))

result = []
s = 0
e = len(arr)-1
maximum = 0
res = ''
while s<e:
    if a[s]>maximum:
        result.append((a[s], 'L'))
    if a[e]>maximum:
        result.append((a[e], 'R'))
    result.sort()
    if len(result) == 0:
        break
    else:
       res = res + result[0][1]



print(result)