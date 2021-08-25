first = int(input())
length = []
num_list = []
result = [first]
#두번째 수로 50 이하가 오면, 100 45 55 -10 이렇게 음수가 나오므로 최대 개수 불가
for second in range(first//2, first+1):
    result.append(second)
    while True:
        #세번째부터의 값들
        #무조건 맨뒤에서 두번째 - 맨뒤에서 첫번째 만 꺼낼거임
        others = result[-2] - result[-1]
        if others < 0:
            #리저트를 초기화시키면서 브레이크
            break
        result.append(others)
    #나온수들의 리스트
    num_list.append(result)
    length.append(len(result))
    result = [first]

maxIdx = length.index((max(length)))
print(max(length))
for i in num_list[maxIdx]:
    print(i, end=' ')

