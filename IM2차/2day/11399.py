N = int(input())
people = list(map(int,input().split()))
people.sort()
result = 0
for i in range(N):
    for j in range(i+1):
        result += people[j]
print(people)
print(result)    