T = int(input())
for tc in range(T):
    C = int(input())
    money = [25, 10, 5, 1]
    result = []
    for i in range(4):
        result.append(C // money[i])
        C %= money[i]
        print(result[i], end=' ')    