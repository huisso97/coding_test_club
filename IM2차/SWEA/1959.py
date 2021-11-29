import sys
sys.stdin = open('1959.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        maximum = 0
        for i in range(N-M+1):
            summation = 0
            #고정시킬 곳은 여기서는 B
            #긴부분은 하나씩 오른쪽으로 이동해야함
            for j in range(M):
                summation += A[i+j]*B[j]
                # print(A[i+j])
                # print(B[j])
            if maximum < summation:
                maximum = summation
    else:
        maximum = 0
        for i in range(M-N+1):
            summation = 0
            for j in range(N):
                summation += A[j] * B[j+i]
                # print(A[j])
                # print(B[j+1])
            if maximum < summation:
                maximum = summation
    print('#{} {}'.format(tc, maximum))

'''
    T = int(input())

    for tc in range(1, T + 1):
        n, m = map(int, input().split())
        arr_A = list(map(int, input().split()))
        arr_B = list(map(int, input().split()))

        # arr_A를 짧은 리스트로 만들어주기 위해서
        # 만약 arr_A가 arr_B보다 길면 두 개의 값을 바꿔준다.
        tmp = 0
        if len(arr_A) > len(arr_B):
            # 1
            tmp = arr_A
            arr_A = arr_B
            arr_B = tmp
            # 2
            arr_A, arr_B = arr_B, arr_A

        # 계산된 값들을 저장해줄 리스트
        answer = []
        # 벽을 넘지 않는 범위내에서 검색 시작
        for i in range(len(arr_B) - len(arr_A) + 1):  # M-N+1
            # 임시 계산 값을 담아줄 result 임시변수
            result = 0
            # 짧은 리스트의 길이만큼 반복해서 하나는 고정시키고
            # 긴 리스트는 하나씩 오른쪽으로 이동하면서 그 길이만큼 계산
            for j in range(len(arr_A)):  # N
                result += (arr_A[j] * arr_B[i + j])
            # 이렇게 계산된 값을 answer에 담아주고
            answer.append(result)
            # 그 중에서 제일 큰 최대값을 출력해주면 된다.
        print('#{} {}'.format(tc, max(answer)))
'''



















    # #B가 더 길 경우
    # if N < M:
    #     while True:
    #     #A의 인덱스 N에 도착하면 0으로 바꾸기
    #         pivot = 0
    #         #회 당 +1 씩 할거, M-N까지
    #         tmp = 0
    #         idx = 0
    #         maximum = 0
    #         summaition = 0
    #         while True:
    #             if pivot == N:
    #                 break
    #             summaition += A[pivot]*B[idx]
    #             pivot += 1
    #             idx += 1
    #         if summaition > maximum:
    #             maximum = summaition
    #         tmp += 1
    #         idx = tmp
    #         if idx == M-N+1:
    #             break
    # print(maximum)
    # else:
    #     pass