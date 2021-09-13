import sys
sys.stdin = open('2231.txt')

N = int(input())
#sub와 N이 같아질때

for num in range(N):
    sub = num
    for i in str(num):
        #num의 각 숫자들을 더해준다
        sub += int(i)
    if sub == N:
        print(num)
        break
if sub != N:
    print(0)
