N = int(input())
m = int(input())

friends = dict()

for i in range(1, N+1):
    friends[i] = []

for i in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
result = set(friends[1])

for i in friends[1]:
    result.update(friends[i])
    # print(friends[i])
print(len(result)-1)
# for i in range(len(friends)):
#     if 1 in friends[i]:
#         result += len(friends[i])-1
# print(result)(len(friends)):
# #     if 1 in friends[i]:
# #         result += len(friends[i])-1
# # print(result)