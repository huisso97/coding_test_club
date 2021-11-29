#find[알파벳] 해당 알파벳이 적힌 첫번째 인덱스 반환
al = str(input())
li = range(97, 123)
for i in li:
    print(al.find(chr(i)), end=' ')