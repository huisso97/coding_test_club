import sys
sys.stdin = open('17609.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    #if arr == arr[::-1] -> 회문 (조건1)
    #회문인지 확인
    if arr == arr[::-1]:
        print(0)
    else:
        #유사회문 확인
        for i in range(len(arr)):
            tmp = arr.pop(i)
            if arr == arr[::-1]:
                print(1)
                break
            else:
                arr.insert(i, tmp)
            if i == len(arr)-1:
                print(2)
                break
        #일반문자열 확인
    #else:
        #유사회문인지
        #첫번째 인덱스 제거하고 회문인지 체크 ~마지막 인덱스제거까지 체크
            #1  출력 break
        #일반문자열인지
        #2출력 break

    # length = len(arr)//2
    # cnt = 0
    # for i in range(length):
    #     if arr[i] == arr[len(arr)-i-1]:
    #         continue
    #     else:
    #         cnt += 1
    # if cnt == 0 :
    #     print(0)
    #
    # else:
    #     exist = False
    #     normal = False
    #     for j in range(length):
    #         if exist == False and arr[j] != arr[len(arr)-j-1] and arr[j] == arr[len(arr)-j-2] :
    #             arr.pop(len(arr)-i-1)
    #             exist = True
    #         elif exist == False and arr[j] != arr[len(arr)-i-1] and arr[j+1] == arr[len(arr)-j-1]:
    #             arr.pop(j)
    #             exist = True
    #         if arr[j] == arr[len(arr)-j-1]:
    #             continue
    #         else:
    #             normal = True
    #             break
    #
    #     if normal:
    #         print(2)
    #     else:
    #         print(1)

