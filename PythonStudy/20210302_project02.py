# 인스턴스를 만들 때 값 받기
'''
class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2
'''

class Person:
    def __init__(self, name, position, team, address):
        self.name = name
        self.position = position
        self.team = team
        self.__address = address # 비공개 속성은 .__와 같이 사용하자(private 접근지정과 비슷한 효과)

    def information(self):
        print('name: {0}, position: {1}, team: {2}'.format(self.name, self.position, self.team))

messi = Person('Messi', 'FW', 'FC_Barcelona', 'address')
messi.information()

print('이름:', messi.name)
print('포지션:', messi.position)
print('소속팀:', messi.team)
# print(messi.__address)는 접근 불가로 에러발생


# 매개변수 self가 특이하지 나머지와 기타 사용법들은 기존에 알고있던 cpp나 java와 비슷하니 이렇게 이해하면 좋을 것 같다.
