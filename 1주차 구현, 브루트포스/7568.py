#rank로 들어온 값보다 더 작으면 rank +=1 해준다
n = int(input())

people = []

for _ in range(n):
    people.append(list(map(int,input().split())))
# print(people)


for i in range(len(people)):
    rank = 1
    for j in range(len(people)):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    print(rank, end=' ')
