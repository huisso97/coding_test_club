N = int(input())

for number in range(N):
    sub = number
    for num in str(number):
        sub += int(num)
    if sub == N:
        print(number)
        break