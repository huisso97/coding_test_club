for tc in range(1, T+1):
    N, M = (map(int, (input().split())))
    # N개의 정수 배열
    # N개의 배열수, M개 이웃
    gugan = list(map(int, input().split()))
    #gugan = [N개의 정수 배열]
    #이웃한 갯수만큼 순회
    li = []
    for i in range(N-2):
        #이웃한 수 더한 값 li에 더한 후, 최대값과 최소값 구해서 차이 반환
        li.append(range(gugan[i], gugan[i+M-1]))
    result = max(li) - min(li)
print('#{}: {}'.format(tc, result))