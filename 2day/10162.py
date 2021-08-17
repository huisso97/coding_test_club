T = int(input())

time = [300, 100, 10]

button = []*3

for i in range(len(time)):
    button.append(T // time[i])
    T %= time[i]
if T == 0:
    print(button[0], button[1], button[2])
else:
    print(-1)