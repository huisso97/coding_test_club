n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    cnt = 0
    for number in range(numbers[0], numbers[1]+1):
        for num in list(str(number)):
            if num == '0':
                cnt +=1
    print(cnt)