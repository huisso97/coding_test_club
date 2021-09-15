import sys
sys.stdin = open('2309.txt')


small_guys = []
for _ in range(9):
    small_guys.append(int(input()))
# print(small_guys)

fake = []
exist = False
for i in range(9):
    for j in range(9):
        if i != j and 100 + (small_guys[i]+small_guys[j]) == sum(small_guys):
            fake.append(small_guys[i])
            fake.append(small_guys[j])
            exist = True
            break
    if exist:
        break

small_guys.sort()
for guys in small_guys:
    if guys not in fake:
        print(guys)