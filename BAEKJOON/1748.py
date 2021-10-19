num = int(input())
result = []
i = 1
while True:
    if i == num:
        result.append(str(i))
        break
    result.append(str(i))
    i += 1
ans = ''.join(result)

print(len(ans))
