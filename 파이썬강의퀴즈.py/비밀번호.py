# address = input()
# a = address[7:-4]
# k = a.count('e')
# print(a[:3] + str(len(a)) + str(k) + '!') 


# url = 'http://naver.com'
# #1 http:// 제외
# my_str = url.replace('http://', '') 
# #2 mystr의 처음부터 처음 .나오는 전까지 자른다
# my_str = my_str[:my_str.index('.')]
# #3 
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
# print('{}의 password는 {}입니다.'.format(url, password))

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자 생성
# users = list(users)
# shuffle(users) #랜덤 섞음

# winners = sample(users, 4) #4명 무작위 뽑음
# print("치킨 당첨자 {0} 과 커피 당첨자들 {1} 축하드립니다.".format(winners[0], winners[1:]))

# customer = '토르'
# index = 5
# while index >= 1: #조건식이 들어감
#     print('{}, 커피가 {}번 남았어요.'.format(customer, index))
#     index -= 1
#     if index ==0:
#         print('커피')

#  #결석한  사람
# absent = [2, 5]

#  #출석을 부르는데, 결석한 사람 빼고 부른다
# for stundent in range(1, 11):
#     if stundent in absent:
#         continue # 학생이 결석했으면 밑에 출력안하고 그 다음 반복문 실행
#     print('{}아, 책을 읽어봐.'.format(stundent))

# student = [ len(i) for i in student]

from random import *
count = 0
for i in range(1,51) : 
    a = randrange(5,51)
    if 5<= a <= 15:
        print('[o] {} 번째 손님 (소요시간 : {})'.format(i, a) )
        count +=1
    else:
        print('[] {} 번째 손님 (소요시간 : {})'.format(i, a) )
print('총 탑승 승객 : {}'.format(count))

# gun = 10
# def checkpoint(gun, solidiers):
#     gun = gun - solidiers
#     print('남은 총의 개수는 {}입니다'.format(gun))
#     return gun
# gun = checkpoint(gun, 2)
# print(gun)

# def std_weight(m, sex):
#     if sex == '남':
#         return m * m * 22
#     else:    
#         return m**2 * 21
# m = 157
# sex = '여자'        
        
# #소수점 둘째자리까지 출력해줘 round(변수, 2)
# i = round(std_weight(m / 100, sex), 2)
# print('키 {0}cm {1}의 표준 체중은 {2}kg입니다.'.format(m, sex, i))

# scores = {'수학':0, '영어':50, '코딩':100}
# for subject, score in scores.items(): #키와 벨류를 튜플 형으로 반환
#     print(subject.ljust(8), str(score).rjust(4), sep=':') 
#     #subject는 8칸 확보한 상태에서 왼쪽 정렬, score은 4칸 확보한 상태에서 
#     #오른쪽 정렬
#     '''
#     수학      :   0
#     영어      :  50
#     코딩      : 100
#     '''

# #은행 대기순번표 001, 002, 003
# for num in range(1,21):
#     print('대기번호 : ' + str(num).zfill(3))
#     #3크기만큼 공간확보하고 빈공간은 0으로 채운다 

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        #유닛으로부터 상속받음 
    def attack(self, location):
        print('{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(self.name, location, self.damage))
        
firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('1시')