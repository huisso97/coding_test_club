n = int(input())


numbers = []
for _ in range(n):
    number = int(input())
    numbers.append(number)
numbers.sort()
for i in range(n):
    print(numbers[i])