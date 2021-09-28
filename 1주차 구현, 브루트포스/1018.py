
#행, 열
n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(input())
#8칸을 넘어갔을 때, 시작 인덱스 1씩 옮겨야함
#인덱스상 0~7까지가 8칸
#n이 9이면 0~9, 1~8 인덱스 체크
result = []
for i in range(n-7):
    for j in range(m-7):
        w_num = 0
        #체스판에서 8*8 볼거임
        for a in range(i, i+8):
            for b in range(j, j+8):
                #체스판 0,0 0,2 0,4 인덱스 합이 짝수인 구간은 같은 색
                #0,0을 w으로 했을 때
                if (a+b)%2==0:
                    #합이 짝수인 인덱스에 w가 아니면 w로 바꾸기
                    if arr[a][b] != 'W':
                        w_num += 1
                #0,1을 b로 지정
                else:
                    #합이 홀수인 인덱스가 B가 아니면
                    if arr[a][b] != 'B':
                        #B로 바꾸기
                        w_num += 1
        result.append(w_num)
        result.append(8*8-w_num)
print(min(result))
