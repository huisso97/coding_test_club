T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    num = []
    num.append(n)
    while True:
        a = n // 10
        b = n % 10
        c = b * 10 + (a + b) % 10
        cnt += 1
        if c == num[0]:
            break
        n = c
    print(cnt)

N = int(input())
start = N
hap = 0 # a + b = hap 2 + 6 = 8
new = 0 # 'b' + 'hap' 6 + 8 = 68
cnt = 0 # 연산되는 횟수
while True:
    hap = N//10 + N%10
    new = (N%10)*10 + hap%10
    N = new
    cnt += 1
    if new == start:
        break
print(cnt)