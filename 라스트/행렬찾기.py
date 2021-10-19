# 가로길이를 찾아준다
def width(i, j):
    # 가로 길이를 카운트
    count = 1
    # x값은 우리가 받아온 값에서 j를 넣어준다. 이유는 알지?
    x = j
    # 반복문 돌면서 계속 받아온 그 값에 0이 아닌 값이 있다면 계속 이어서 돈다.
    while True:
        x += 1
        if x >= N:
            break
        if map_list[i][x]:
            count += 1
        else:
            break
    return count

# 마찬가지 방법으로 세로길이 탐색
def height(i, j):
    count = 1
    y = i
    while True:
        y += 1
        if y >= N:
            break
        if map_list[y][j]:
            count += 1
        else:
            break
    return count

# 탐색한 부분의 값 0으로 변경
def change(s_y, s_x, e_y, e_x):
    for i in range(s_y, e_y):
        for j in range(s_x, e_x):
            map_list[i][j] = 0


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    # 리스트 내포기능으로 반복해서 입력받음
    map_list = [list(map(int, input().split())) for _ in range(N)]
    answer_list = []
    for i in range(N):
        for j in range(N):
            # 값이 있다면
            if map_list[i][j]:
                # 가로길이 받아오고
                w = width(i, j)
                # 세로길이 받아와서
                h = height(i, j)
                # 리스트 내용바꿔주고
                change(i, j, i + h, j + w)
                # 행열 크기 넣어주고 곱한값 넣어주고
                answer_list.append([h, w, h * w])
    # 출력해야 하니까 정렬해야 하는데 곱한값 기준으로 오름차순, 다음은 행렬 크기로 오름차순
    answer_list = sorted(answer_list, key=lambda x: (x[2], x[0]))
    # 이 밑에는 출력하기
    print('#{} {}'.format(t, len(answer_list)), end=' ')
    for r, c, _ in answer_list:
        print('{} {}'.format(r, c), end=' ')
    print()