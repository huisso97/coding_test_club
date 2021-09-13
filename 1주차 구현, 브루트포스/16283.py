a, b, n, w = map(int, input().split())

lamb = 1
goat = 1
animals = []
while True:
    if n == lamb + goat and w == lamb*a + goat*b:
        animals.append([lamb, goat])
    else:
        lamb += 1
        goat += 1

for i in range(n):
    for j in range(n-i):

