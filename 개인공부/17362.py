n = int(input())

#검지 기준 8회 주기를 가짐
result = n % 8
if result == 1:
    print(1)
elif result == 2 or result == 0:
    print(2)
elif result == 3 or result == 7:
    print(3)
elif result == 4 or result == 6:
    print(4)
elif result == 5:
    print(5)
