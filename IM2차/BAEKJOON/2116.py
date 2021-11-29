import sys
sys.stdin = open('input.txt')

# 옆면의 최대 값을 구한다
# ABCDEF 순서에 맞게 숫자를 입력 받는다.
# 아래 주사위의 윗면과 위 주사위의 아랫면이 같은 수여야 한다.
# 1번 주사위를 기준으로 위는 그냥 자연스럽게 따라온다고 생각하면 된다.
# 그래서 1번 주사위를 6가지 방법으로 둔 상태에서 주사위가 쌓일텐데 그 때 옆면 최대값을 구한 후 배열에 넣고
# 가장 큰 값을 뽑아내면 된다.
# 만약 a를 윗면 기준으로 삼는다면 a를 변수 tmp 에 넣어주고 다음에 들어오는 값 중 tmp와 같은 값을 제거하고 밑으로 기준 삼고
# 그 마주보는 면을 다시 변수 tmp 에 넣어주고 다음 input값에서 tmp와 같은 걸 제거하고 마주보는 값을 tmp에 넣고 제거 반복
# 제거 하면서 주사위 마다의 남은 값들을 list에 넣어주고 그 값들을 모두 담은 후 최고 큰 값들을 가지고 와서 기준마다의
# 옆면 합을 다시 list에 담아서 그 중 최고 큰 값을 가져오면 된다.
# 딕셔너리 사용

dice = []
result_list = []
c = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

n = int(input())
for _ in range(n):
    dice.append(list(map(int, input().split())))

for k in range(6):
    tmp = dice[0][k]
    numbers = []
    result = 0
    for i in range(len(dice)):
        for j in range(6):
            if dice[i][j] == tmp:
                tmp_numbers = []
                for z in dice[i]:
                    if z == dice[i][j] or z == dice[i][c[j]]:
                        continue
                    else:
                        tmp_numbers.append(z)
                numbers.append(tmp_numbers)
                tmp = dice[i][c[j]]

    for i in range(n):
        result += max(numbers[i])
    result_list.append(result)

print(max(result_list))