import sys
sys.stdin = open('1244.txt')

N = int(input())
switch = [0]+list(map(int, input().split()))
num = int(input())
student = []
for i in range(num):
    student.append(list(map(int, input().split())))

for i in range(num):
    if student[i][0] == 1:
        check = student[i][1]
        n = 1
        while True:
            a = check*n
            if a >= len(switch):
                break
            if switch[a] == 1:
                switch[a] = 0
            else:
                switch[a] = 1
            n += 1
    if student[i][0] == 2:
        check = student[i][1]
        n = 0
        while True:
            if 0 < check-n and check+n<len(switch) and switch[check-n] == switch[check+n]:
                if switch[check-n] == 0:
                    switch[check-n] = 1
                    switch[check+n] = 1
                else:
                    switch[check-n] = 0
                    switch[check+n] = 0
                n += 1
            else:
                break
switch.pop(0)
while True:
    if len(switch) > 20:
        print(*switch[:20])
        del switch[:20]
    else:
        print(*switch)
        break
