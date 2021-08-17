static, time, price = map(int, input().split())
x = 0
while True:
    x += 1
    cost = static + time*x
    benefit = price*x
    if cost < benefit:
        break
    else:
        continue
print(x)
