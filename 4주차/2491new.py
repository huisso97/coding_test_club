import sys
sys.stdin = open('2491.txt')

N = int(input())
#수열 길이 비교 멕시멈
maximum = -1

number = list(map(int, input().split()))
#수열 담을 리스트
arr_1 = [] #커지는 수열
sub_1 = 1
for i in range(len(number)-1):
    if number[i] <= number[i+1]:
        sub_1 += 1
    else:
        arr_1.append(sub_1)
        sub_1 = 1
#길이가 1인 애 넣어
arr_1.append(sub_1)

arr_2 = []
sub_2 = 1
for i in range(len(number)-1):
    if number[i] >= number[i+1]:
        sub_2 += 1
    else:
        arr_2.append(sub_2)
        sub_2 = 1
#너도 넣어
arr_2.append(sub_2)

# print(arr_2, arr_1)
print(max(max(arr_1), max(arr_2)))

'''
N = int(input())
#수열 길이 비교 멕시멈
maximum = -1

number = list(map(int, input().split()))
#수열 담을 리스트
arr = []

for i in range(len(number)-1):
    if number[i+1] - number[i] >= 0:
        arr.append(number[i])
    else:
        if len(arr) > maximum:
            maximum = len(arr)
        arr = []
for i in range(len(number)-1):
    if number[i] - number[i+1] >= 0:
        arr.append(number[i + 1])
        
    else:
        if len(arr) > maximum:
            maximum = len(arr)
        arr = []

if maximum >= 3:
    print(maximum)
else:
    print(2)

'''
