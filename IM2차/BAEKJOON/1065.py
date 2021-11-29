number = input()

result = 0
if len(number) <= 2:
    result = int(number)
else:
    result = 99
    for num in range(100, int(number)+1):
        tmp = str(num)
        if int(tmp[1])-int(tmp[0]) == int(tmp[2])-int(tmp[1]):
            result += 1
print(result)
