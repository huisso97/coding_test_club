import sys
sys.stdin = open('1206.txt')

for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    #건물 기준으로 앞2칸 뒤2칸 나보다 낮으면, 그 중 가장 높은건물 기준 으로 내랑 얼만큼 차이나는지 체크해서 넣기
    result = 0
    for i in range(2, len(arr)-2):
        if arr[i-2]<arr[i] and arr[i-1]<arr[i] and arr[i]>arr[i+1] and arr[i]>arr[i+2]:
            tmp = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
            result += arr[i]-tmp
    print('#{} {}'.format(tc, result))