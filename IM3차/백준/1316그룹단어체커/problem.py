import sys
sys.stdin = open('input.txt')

N = int(input())
res = 0
for _ in range(N):
    arr = input()
    letter_list = []
    tmp = 0
    for i in range(len(arr)):
        if arr[i] not in letter_list:
            letter_list.append(arr[i])
            tmp = arr[i]
        elif arr[i] == tmp:
            pass
        elif arr[i] in letter_list:
            break
        if i == len(arr)-1:
            res += 1
print(res)