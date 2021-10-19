import sys
sys.stdin = open('1221.txt')

T = int(input())
for tc in range(1, T+1):
    tc, length = input().split()
    arr = list(input().split())
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    lst = []
    for i in range(len(number)):
        for j in range(len(arr)):
            if arr[j] == number[i]:
                lst.append(arr[j])

    print('{}'.format(tc))
    for i in lst:
        print(i, end=' ')
    print()