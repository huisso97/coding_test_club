import sys
sys.stdin = open('2559.txt')

N, K = map(int, input().split())
tempartures = list(map(int, input().split()))
print(te)
maximum = sum(tempartures[:K])
result = sum(tempartures[:K])
temp = tempartures[:K]
#맨첫번째 빼고, 맨뒤에 넣고 해서 값 비교하기
while K < N:
    a = temp.pop(0)
    result -= a
    result += tempartures[K]
    temp.append(tempartures[K])
    K = K + 1
    if maximum < result:
        maximum = result
print(maximum)