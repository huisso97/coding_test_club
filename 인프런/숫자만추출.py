N = input()
number = 0
for i in N:
    if i.isdecimal():
        number = number*10 + int(i)
        print(number)
result = []
for num in range(1, number+1):
    if number % num == 0:
        # result += 1
        result.append(num)
print(len(result))
