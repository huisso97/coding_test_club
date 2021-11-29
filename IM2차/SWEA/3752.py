import sys
sys.stdin = open('3752.txt')
#조합문제
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(set(list(map(int, input().split()))))
    # score.sort(reverse=True)
    #
    # check = [0 for _ in range(score[0]+1)]
    # #점수에 해당하는 각 인덱스 True
    # for i in range(len(score)):
    #     check[score[i]] = True
    result = [0]
    length = 1
    while length != N:
        summation = 0
        for i in range(len(score)):
            tmp = 0
            while tmp !=length:
                summation += score[i]
                result.append(summation)
                summation = 0
                tmp += 1
            tmp = 0
        length += 1
    print(result)

    '''
    [5, 3, 2]
    [0, 0, True, True, 0, True]
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    [0, True]
    '''

