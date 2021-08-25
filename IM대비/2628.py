#가로 세로 길이
x, y = map(int, input().split())

# paper = list([False for i in range(column)] for _ in range(row))
#간격들을 구하는 for문에서 별도의 예외처리를 안하기 위해 0을 넣어줌
xArr, yArr = [0],[0]
# #칼로 잘라야하는 점선의 개수
N = int(input())
for _ in range(N):
    val, num = map(int, input().split())
    #x축으로 자르면 y배열에 y축으로 자르면 x배열에 넣어줌
    if val == 0:
        yArr.append(num)
    else:
        xArr.append(num)
# print(xArr, yArr)  [0, 4] [0, 3, 2]
# #정렬
xArr.sort()
yArr.sort()

#간격들을 구하는 for문에서 별도의 예외처리를 안하기 위해 각 길이를 넣어줌
xArr.append(x)
yArr.append(y)
# print(xArr, yArr) [0, 4, 10] [0, 2, 3, 8]

#초기값
xMaxInterval = xArr[1] - xArr[0]
yMaxInterval = yArr[1] - yArr[0]

#가장 넓은 구간 구하기
for xIdx in range(2, len(xArr)):
    xMaxInterval = max(xMaxInterval, xArr[xIdx]-xArr[xIdx-1])
for yIdx in range(2, len(yArr)):
    yMaxInterval = max(yMaxInterval, yArr[yIdx]-yArr[yIdx-1])

print(xMaxInterval*yMaxInterval)

# x,y = map(int,input().split()) # 입력
#
# #간격들을 구하는 for문에서 별도의 예외처리를 안하기 위해 0을 넣어줌
# xArr,yArr = [0],[0]
#
# m = int(input())
# for i in range(m):
#   val, num = map(int, input().split())
#   # x축으로 자르면 y배열에 y축으로 자르면 x 배열에 넣어준다.
#   if val == 0 :
#     yArr.append(num)
#   else :
#     xArr.append(num)
#
# # 정렬
# xArr.sort()
# yArr.sort()
#
# #간격들을 구하는 for문에서 별도의 예외처리를 안하기 위해 각 길이를 넣어줌
# xArr.append(x)
# yArr.append(y)
#
# # 초기값
# xMaxInterval = xArr[1] - xArr[0]
# yMaxInterval = yArr[1] - yArr[0]
#
# # 가장 넓은 구간 구하기
# for xIdx in range(2,len(xArr)):
#   xMaxInterval = max(xMaxInterval,xArr[xIdx] - xArr[xIdx-1])
#
# for yIdx in range(2,len(yArr)):
#   yMaxInterval = max(yMaxInterval,yArr[yIdx] - yArr[yIdx-1])
#
# # 정답 출력
# print(xMaxInterval*yMaxInterval)
