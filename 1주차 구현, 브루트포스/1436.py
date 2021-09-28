n = int(input())

number = 666
cnt = 0
# 666,1666,2666,3666,4666,5666,6660, 6661, 6662, 6666,7666
while True:

    if '666' in str(number):
        cnt += 1
    if cnt == n:
        print(number)
        break
    number += 1