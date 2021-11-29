import sys
sys.stdin = open('p.txt')

arr = list(input())
number = ['0','1','2','3','4','5','6','7','8','9']
arr.sort()
summation = 0
result = []
for i in arr:
    if i in number:
        summation += int(i)
    else:
        result.append(i)
result.append(summation)
for i in range(len(result)):
    print(result[i], end='')
