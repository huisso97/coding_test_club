import sys
sys.stdin = open('2635.txt')

num1 = int(input())
for i in range(1, num1):
    arr = [num1]
    num2 = num1
    arr.append(i)
    num2 = num1 - i
    arr.append(num2)
    num3 = num1 - num2
    arr.append(num3)
    tmp = 0
    while tmp > 0:
        tmp = num2-num3
        if tmp < 0:
            break
        arr.append(tmp)
        num2 = num3
        num3 = tmp

    print(arr)