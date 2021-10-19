number = int(input())
result = [number]
length = []
maximum = 0
for i in range(number//2, number+1):
    result.append(i)
    while True:
        num = result[-2]-result[-1]
        if num<0:
            break
        result.append(num)
    if len(result)>maximum:
        maximum = len(result)
        length = result
    result = [number]
print(maximum, length)