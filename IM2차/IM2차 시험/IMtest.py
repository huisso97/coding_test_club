import sys
sys.stdin = open('sample_input.txt')
T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #sx,sy의 값 = 시작숫자 = num
    #전체순회하여 num과 같으면 (x-sx)*(y-sy) 을 담아 그리고 maximum과 비교
    #maximum 하면 이제 그 맥시멈과 같은 애들만 찾아서 리스트에 담기
    num_list = [i for i in range(0, 1000)]
    maximum = -100000000
    lst = []
    for sy in range(N):
        for sx in range(N):
            #시작숫자
            num = arr[sy][sx]

            #체크한 숫자는 패스
            # if num in num_list:
            #     num_list.remove(num)
            # print(num_list)
            big = 0
            idx_list = []
            for y in range(N):
                for x in range(N):
                    same = arr[y][x]
                    if num == same:
                        big = (abs(sx-x)+1)*(abs(sy-y)+1)
                        idx_list = [sy, sx, y, x]
                        # print(big)
                        # print(x,y,sx,sy)
                        # print(abs(sx-x), abs(sy-y))
            if maximum < big:
                maximum = big
                lst.append([idx_list, big])


    print(lst)
    print('done', maximum)
    num_list = [i for i in range(0, 1000)]


    result = 0
    for sy in range(N):
        for sx in range(N):
            # 시작숫자
            cnt = 0
            num = arr[sy][sx]
            # 체크한 숫자는 패스
            # if num in num_list:
            #     num_list.remove(num)
            big = 0
            for y in range(N):
                for x in range(N):
                    same = arr[y][x]
                    if num == same:
                        big = (abs(sx - x)+1) * (abs(sy - y)+1)
                        if big == maximum:
                            cnt += 1


    print('#{} {}'.format(tc, result))