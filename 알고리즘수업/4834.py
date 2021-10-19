import sys
sys.stdin = open('4834.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(input())

    maximum = 0
    for i in range(len(number)):
        if int(number[i]) > maximum:
            maximum = int(number[i])
    #카드 수 세는 리스트
    result = [0]*(maximum+1)
    for i in range(len(number)):
        card = int(number[i])
        result[card] += 1
    # print(result)
    maximum = 0
    max_idx= 0
    for i in range(len(result)):
        if result[i] >= maximum:
            maximum = result[i]
            max_idx = i
    print('#{} {} {}'.format(tc, max_idx, maximum))