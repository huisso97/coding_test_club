import sys
sys.stdin = open('1213.txt', 'rt', encoding='UTF8')

for _ in range(1, 11):
    tc = int(input())
    find = input()
    line = input()

    cnt = 0

    for i in range(len(line)-len(find)+1):
        if line[i:i+len(find)] == find:
                cnt += 1
                # print(line[i:i+len(find)])
    print('#{} {}'.format(tc, cnt))