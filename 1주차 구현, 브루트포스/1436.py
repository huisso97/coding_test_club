n = int(input())


result = []
i = 665
while True:
    if '666' in str(i):
        result. append(i)
    i += 1
    if len(result) == n:
        break
print(result[n-1])