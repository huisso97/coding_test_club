import sys
sys.stdin = open('6190.txt')


#곱한 값이 단조증가수인지 확인해서 맞으면, 모아서 그 중 곱의 최댓값 구하기
#없으면 -1

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = []
    for i in range(0, len(arr)-1):
        num = arr[i]*arr[i+1]
        if len(str(num)) == 1:
            tmp.append(num)
        else:
            for j in range(0, len(str(num))-1):
                if int(num[j]) < int(num[j+1]):
                    tmp.append(num)
    # print(tmp)








# if result:
#     print('#{} {}'.format(tc, result))

