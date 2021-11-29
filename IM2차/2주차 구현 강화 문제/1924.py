x, y = map(int, input().split())

day = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
#0번째 인덱스가 0인 이유는 밑의 포문에서 x가 1월일 때는 y값만 더해줘야하므로
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum = 0
#해당 월까지의 일수들을 다 던한다
for i in range(x):
    sum += month[i]
sum += y

sum %= 7
#-1을 하는 이
print(day[sum])