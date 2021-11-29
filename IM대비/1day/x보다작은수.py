input_data = input().split(' ')
n = int(input_data[0])
x = int(input_data[1])
# 1 5 3  4
# ['1', '5', '3', '4']
# [1, 5, 3, 4]
a = list(map(int, input().split(' ')))

for i in a :
    if x > i :
        print(i)
