import sys
sys.stdin = open('17127.txt')

n = int(input())

forest = list(map(int, input().split()))
maximum = 0
for i in range(1, len(forest)):
    for k in range(i+1, len(forest)):
        for j in range(k+1, len(forest)):
           if maximum < sum(forest[:i] + forest[i+1:k] + forest[k+1:j] + forest[j+1:]):
               maximum = sum(forest[:i] + forest[i+1:k] + forest[k+1:j] + forest[j+1:])
print(maximum)
