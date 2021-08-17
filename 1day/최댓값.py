# taking 9 input at a time (list comprehension)
a = [int(x) for x in input().split(',')]

max_a = a[0]
for i in range(len(a)):
    if max_a < a[i]:
        max_a = a[i]
print(max_a)
print(i)