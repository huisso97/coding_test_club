import sys
sys.stdin = open('4861.txt')

T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
#     board = [list(input()) for _ in range(N)]
#
#     #가로탐색
#     result = []
#     for i in range(N):
#         for j in range(N-M+1):
#             tmp = board[i][j:j+M]
#             if tmp == tmp[::-1]:
#                 result.append(tmp)
#     #세로탐색
#     tmp = []
#     for i in range(N):
#         for j in range(N-M+1):
#             for k in range(M):
#                 tmp.append(board[j+k][i])
#             if tmp == tmp[::-1]:
#                 result.append(tmp)
#             tmp = []
#     # print(tmp)
#     print('#{}'.format(tc), end=' ')
#     print(''.join(result[0]))

for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_list = [input() for _ in range(N)]
    # 세로줄을 담아낼 빈 리스트
    str_vertical = []
    # 최종 회문을 받아낼 리스트
    result = []
    # zip(*args)는 배열에서 행이 아닌 열을 순서대로 가져올 수 있게 해주는 함수로 활용가능
    for vertical in zip(*str_list):
        print(vertical)
        # 세로줄을 모두 str_list에 넣어주고 한번만 비교하면 된다.
        str_list.append(''.join(vertical))
    # 세로줄까지 넣어줬으므로 인덱스는 str_list 길이만큼 진행
    for i in range(len(str_list)):
        # j+M 번째까지 확인하기 때문에 M을 빼준 후 인덱스 이므로 +1을 추가
        for j in range(N-M+1):
            # 문자열과 뒤집은 문자열이 일치하는지 확인 후 결과값에 추가
            if str_list[i][j:j+M] == str_list[i][j:j+M][::-1]:
                result.append(str_list[i][j:j+M])
    print('#{} {}'.format(tc, ''.join(result)))
