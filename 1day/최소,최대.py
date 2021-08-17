a = int(input())
b = list(map(int, input().split(' ')))
min_b = b[0]
max_b = b[0]
for i in range(a):
    if max_b < b[i] :
        max_b = b[i]
for i in range(a):
    if min_b > b[i]:
        min_b = b[i] 

print(min_b, max_b)