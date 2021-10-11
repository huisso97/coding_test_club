import sys
sys.stdin = open('16922.txt')
number = [1, 5, 10, 50]
count = [0, 0, 0, 0]
#합 중복x조합?
n = int(input())
result = []
idx = 0
summation = 0
while True:
    for i in range(len(number)):
        for j in range(len(number)):
            summation += number[i+j]
            count[i+j] += 1
    if sum(count) == n:
        result.append(summation)
        summation = 0
        idx += 1

# def find(depth):
#     #기저
#     if depth == n:
#         if sum(tmp) not in result:
#             result.append(sum(tmp))
#             return
#         else:
#             return
#     else:
#         for i in range(len(number)):
#             tmp.append(number[i])
#             find(depth+1)
#             tmp.pop()
# find(depth)
# print(len(result))