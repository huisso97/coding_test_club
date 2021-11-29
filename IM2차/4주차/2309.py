import sys
sys.stdin = open('2309.txt')

short = []
for i in range(9):
    short.append(int(input()))

short.sort()

exist = False
for i in range(9):
    for j in range(9):
        if 100 + short[i] + short[j] == sum(short):
            tmp1 = short[i]
            tmp2 = short[j]
            short.remove(tmp1)
            short.remove(tmp2)
            exist = True
            break
    if exist == True:
        break
for i in short:
    print(i)
