
T = int(input())

for tc in range(T):
    R, S = input().split()

    for char in S:
        for i in range(int(R)):
            print(char, end='')
    print()