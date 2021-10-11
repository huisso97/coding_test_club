# break point 걸기 : ctrl + f8
# 디버그모드 진입 : shift + f9
# step over (한줄단위로 실행하기): F8
# step into ( 함수 내부로 들어가기) : F7
# step return ( 함수 실행후 빠져 나오기 ) : shift + F8
# resume ( 다음 브레이크 포인트로 실행 옮기기) : F9
# run to cursor (커서 위치로 실행 옮기기 ) : Alt + F9

def over():
    for i in range(10):
        print("#", end='')
    print("OVER")
    return
def into():
    print("INTO")
    return
into()
into()
into()
over()
over()
into()
over()
into()
over()
over()
print("FINISH")