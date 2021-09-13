import sys
sys.stdin = open('7568.txt')
n = int(input())

people = []
for _ in range(n):
    person = list(map(int, input().split()))
    people.append(person)

maximum = [0, 0]

for i in range(len(people)):
    for j in range(i+1, len(people)):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1] and people[i][0] > maximum[0] and people[i][1] > maximum[1]:
            maximum = people[i]
        else:
            maximum = people[j]

print(maximum)