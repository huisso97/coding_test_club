import sys
sys.stdin = open('1209.txt')

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, 11):

    count = int(input())
    imap = list(map(int, input().split()))
    imap.sort()
    # print(imap)
    # queue = collections.deque(imap)
    # print(queue)

    hmax = 0
    hmin = 100

    for i in range(count):
        # queue.append((queue.pop() - 1))
        # queue.appendleft((queue.popleft() + 1))
        imap[99] -= 1
        imap[0] += 1
        imap.sort()

        # queue.sort()

    for i in range(100):
        hmin = min(hmin, imap[i])
        hmax = max(hmax, imap[i])

    result = hmax - hmin
    print('#{} {}'.format((test_case, result))