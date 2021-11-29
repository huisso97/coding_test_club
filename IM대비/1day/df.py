

# for tc in range(1, 11):
# 가로 길이 1000이하 양쪽 두칸 건물 안지음
width = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(2, (len(numbers)-3)):
    if abs(numbers[i]-numbers[i+1])>=2 and abs(numbers[i])-numbers[i+2])>=2:
        if abs(numbers[i]-numbers[i-1])>=2 and abs(numbers[i]-numbers[i-2])>=2:
            count+=1
#맨 마지막 빌딩은 왼쪽 공백만 체크해서 높이 차가 2 이상이면 1더함
if abs(numbers[-2]-numbers[-3]) >= 2 and abs(numbers[-2]-numbers[-4]) :
    count+1
print(count)