import sys
sys.stdin = open('input.txt')
x, y = map(int, input().split())
# tmp = {'1,3,5,7,8,10,12': 31, '4,6,9,11' : 30,/ '2':28 }
tmp = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
cnt = y-1
for i in range(1, x):
    cnt += tmp[i]
cnt  = cnt%7
print(days[cnt])