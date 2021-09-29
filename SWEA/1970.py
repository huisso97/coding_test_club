import sys
sys.stdin = open('1970.txt')

#5만, 1만, 5천, 1천, 5백, 1백, 5십, 1십


T = int(input())

for tc in range(1, T+1):
    result = [0] * 8
    money = (int(input()))
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count = 0

    for i in range(len(arr)):
        if money // arr[i]:
            result[i] = (money // arr[i])
            money %= arr[i]
        else:
            pass
    print('#{}'.format(tc))
    print(*result)

