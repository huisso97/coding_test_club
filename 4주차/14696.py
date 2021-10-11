import sys
sys.stdin = open('14696.txt')

N = int(input())
for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_num = a[0]
    b_num = b[0]
    a_card = a[1:]
    b_card = b[1:]
    if a_card.count(4) > b_card.count(4):
        print('A')
    elif a_card.count(4) < b_card.count(4):
        print('B')
    elif a_card.count(3) > b_card.count(3):
        print('A')
    elif a_card.count(3) < b_card.count(3):
        print('B')
    elif a_card.count(2) > b_card.count(2):
        print('A')
    elif a_card.count(2) < b_card.count(2):
        print('B')
    elif a_card.count(1) > b_card.count(1):
        print('A')
    elif a_card.count(1) < b_card.count(1):
        print('B')
    else:
        print('D')
