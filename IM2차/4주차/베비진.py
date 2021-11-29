import sys
sys.stdin = open('베비진.txt')

T = int(input())

for _ in range(1, T+1):
    arr = list(input())
    card = [0]*10
    triplet = 0
    run = 0
    for i in range(len(arr)):
        card[int(arr[i])] += 1
    for i in range(len(card)):
        while True:
            if card[i] >= 3:
               triplet += 1
               card[i] -= 3
            else:
                break

    for i in range(1, len(card)-2):
        while True:
            if card[i-1] >=1 and card[i] >= 1 and card[i+1] >= 1:
                run += 1
                card[i - 1] -= 1
                card[i] -= 1
                card[i + 1] -= 1
            else:
                break
    if triplet + run >= 2:
        print('babygin')
    else:
        print('fail')