import sys
sys.stdin = open('swtich.txt')

n = int(input())
switch = [0]+list(map(int, input().split()))
students = int(input())
student = [list(map(int, input().split())) for i in range(students)]
# print(student)
for i in range(students):
    num = student[i][1]
    if student[i][0] == 1:
        for j in range(num, len(switch), num):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0
    elif student[i][0] == 2:
        k = 0
        while True:
            if num-k > 0 and num+k < len(switch) and switch[num-k] == switch[num+k]:
                if switch[num-k] == 0:
                    switch[num-k], switch[num+k] = 1, 1
                else:
                    switch[num-k], switch[num+k] = 0, 0
            else:
                break
            k += 1
switch = switch[1:]
while True:
    if len(switch)>20:
        print(*switch[:20])
        del switch[:20]
    else:
        print(*switch)
        break

#하.......