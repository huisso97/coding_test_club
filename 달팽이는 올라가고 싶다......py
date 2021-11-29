T = int(input())

for tc in range(1, T+1):
    a, b, v = map(int, input().split())
    day = (v-b)/(a-b) # 마지막 밤이 오기 전 올라가는 일수
    print(day)
    if day == int(day):
        print(int(day))
    else:
        print(int(day+1))