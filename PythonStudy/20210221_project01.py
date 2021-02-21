# 함수 사용하기
'''
파이썬에서 함수는 다음과 같이 만든다.

def 함수이름():
    코드
'''
def hello():
    print('Hello, world!')
hello()

'''
함수의 실행순서?

1. 파이썬 스크립트 최초 실행
2. hello 함수 호출
3. hello 함수 실행
4. print 함수 실행 및 'Hello, world!' 출력
5. hello 함수 종료
6. 파이썬 스크립트 종료

파이썬 코드는 위에서 아래로 순차적으로 실행되기 때문에,
반드시 함수를 먼저 만든 뒤에 함수를 호출해야한다.
'''

# 함수의 결과를 반환하기
def add(a, b):
    return a + b
x = add(10, 20)
print(x)

# 값을 여러 개 반환하는 것도 가능하다
# 튜플이 변수 여러 개에 할당되는 특성을 이용한다.
def add_sub(a, b):
    return a + b, a - b
x, y = add_sub(440, 502)
print(x, y)

# 실제로는 튜플이 반환된다.
# 결과를 변수 한 개에 저장해서 출력해보면 알 수 있다.
x = add_sub(230, 130)
print(x)

# 몫과 나머지를 구하는 함수 만들기
x = 10
y = 3
def get_quotient_remainder(a, b):
    return a // b, a % b
quotient, remainder = get_quotient_remainder(x, y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))

# 함수의 호출과정은 반드시 알아두자
# 스택 다이어그램, 전역 프레임, 스택 프레임
