import sys
sys.stdin = open('4865.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()

    result = [0]*len(str1)
    for i in range(len(str1)):
        for j in range(len(str2)):
             if str1[i] == str2[j]:
                 result[i] += 1
    print('#{} {}'.format(tc, max(result)))

T = int(input())

for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = input()
    # str1에 들어있는 각 글자들이 몇개씩 들어있는지 빈 리스트에 넣어놓고 가장 큰 수를 뽑아낸다.
    result = []
    for i in range(len(str1)):
        result.append(str2.count(str1[i]))
    print('#{} {}'.format(tc, max(result)))