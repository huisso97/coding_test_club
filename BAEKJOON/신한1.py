import sys
sys.stdin = open('신한1.txt')

arr = list(map(int, input().split()))

result = 0

for num in arr:
    result += num**2

print(result//10)