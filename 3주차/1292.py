import sys
sys.stdin = open('1292.txt')

start, end = map(int, input().split())

array = []
for i in range(1, 1000):
    for j in range(i):
        array.append(i)
print(sum(array[start-1:end]))