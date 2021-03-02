# 클래스 만들기
# 함수를 만드는 규칙과 비슷하다. 다만 클래스 이름은 대문자로 시작한다.
'''
class 클래스이름:
    def 메소드(self):
        코드
'''
class Person1:
    def greeting1(self):
        print('Hello')

# 나머지 사용방식은 다음과 같이 cpp나 java와 비슷하게 사용하면 된다.
# 인스턴스 = 클래스()
james = Person1()

# 인스턴스.메소드()
james.greeting1()

# 참고로 int, list, dict도 사실 클래스이다.
# 인스턴스를 만들어 메소드를 사용했지만 이 사실을 인지하자.
# 객체만 지칭할 때는 객체(object)가 맞는 표현이고,
# 클래스와 연관지어 지칭할 때는 인스턴스(instance)라고 한다.

# 속성 사용하기
'''
class 클래스이름:
    def __init__(self):
        self.속성 = 값
'''
# __init__ 메소드는 쉽게 말해 다른 객체지향적 언어에서의 생성자라고 생각하자.
# self는 자기 자신을 가리키는 인스턴스인데 다른 언어의 this로 이해하면 쉽다.
# 앞뒤로 __(밑줄 두개)가 붙은 메소드는 파이썬이 자동으로 호출하는 메소드라고한다.
# 스페셜 메소드 혹은 매직 메소드라고 부른다.
class Person2():
    def __init__(self):
        self.hello = '호우!'

    def greeting2(self):
        print(self.hello)

ronaldo = Person2()
ronaldo.greeting2()
