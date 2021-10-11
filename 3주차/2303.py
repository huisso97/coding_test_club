import sys
sys.stdin = open('2303.txt')

n = int(input())

#순서대로 1의 최댓값 담을 것
arr = []
for i in range(n):
    card = list(map(int, input().split()))
    # print(card)
    length = len(card)

    maximum = -1
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                number = str(card[i]+card[j]+card[k])
                if int(number[-1]) > maximum:
                    maximum = int(number[-1])
    arr.append(maximum)

base_idx = 0
base_max = max(arr)
for idx, result in enumerate(arr):
    if result == base_max and idx > base_idx:
        base_idx = idx
print(base_idx+1)