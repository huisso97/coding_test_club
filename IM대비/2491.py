import sys
sys.stdin = open('2491.txt')
n = int(input())
arr = list(map(int, input().split()))
#같거나 커지는 경우 담을 리스트
result1 = []
sub = 1
for i in range(len(arr)-1):
    if arr[i+1] >= arr[i]:
        sub += 1
    else:
        result1.append(sub)
        sub = 1
result1.append(sub)

#같거나 작아지는 경우
result2 = []
sub = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] <= sub[-1]:
        sub.append(arr[i])
    else:
        result2.append(len(sub))
        sub = [arr[i]]

result2.append(len(sub))

print(max(max(result1), max(result2)))

#3가지 조건

#같거나 커지는 경우
    #그 길이가 3 미만일 경우 -> 2출력
#같거나 작아지는 경우
    #그 길이가 3 미만일 경우 -> 2출력