import sys
sys.stdin = open('1769.txt')

x = list(map(int, input()))

cnt = 0
while True:

    if len(x) == 1:
        print(cnt)
        if x[0] in [3, 6, 9]:
            print('YES')
            break
        else:
            print('NO')
            break

    x = list(map(int, list(str(sum(x)))))
    cnt += 1




    # 몇번 바꿔야 1의 자리가 되는지
    # 3의 배수인지