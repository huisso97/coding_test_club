# watch 창에 bin(S)[2:] -> str
# list(bin(S)[2:]) 이거 등록하고 디버깅하기
import sys
sys.stdin = open("11723.txt","r")
N = int(sys.stdin.readline()) # 명령어 개수  , sys.stdin.readline() -> 빠른입력
S = 1 << 21
for _ in range(N):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        cmd, x = temp[0], int(temp[1])
    else :
        cmd = temp[0]
    de = -1
    if cmd == "add":
        S |= (1 << x) # x 번째 bit와 or 연산
    elif cmd == "remove":
        S &= ~(1 << x)  #1을 보낸 후 뒤집어줌
    elif cmd == "check":   #나머지는 0이고 해당 비트만 1인지 체크
        # if S & (1 << x): #01011000 7번비트에 체크되어있는지, 거기까지 1을 가져가서 앤드연산자로 유무 확인
        #     print(1)
        # else:
        #     print(0)
        print((S & (1 << x)) >> x) #빠꾸

    elif cmd == "toggle":
        if S & (1 << x):# 있으면
            S -= (1 << x)
        else:           # 없으면
            S |= (1 << x)
    elif cmd == "all":
        S = (1 << 21)-1 #-1을 하면 전부 다 뒤집혀짐
    elif cmd == "empty":
        S = (1 << 21)