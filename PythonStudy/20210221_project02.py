# 함수의 위치 인수: 함수에 인수를 순서대로 넣는 방식
# 인수의 위치가 정해져 있다는 의미
def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

print_numbers(1, 2, 3)

# 언패킹: 리스트(튜플) 앞에 *를 붙이는 것
# 말 그대로 리스트의 포장을 푼다는 뜻
# 다음과 같이 사용한다.
# 다만, 함수의 매개변수 개수와 리스트의 요소 개수는 같아야 함.
x = [10, 20, 30]
print_numbers(*x)

# 가변 인수 함수 만들기
def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(1, 2, 3)
print_numbers(10)
print_numbers(1, 2, 3.5, 123)

# 키워드 인수를 사용해보자
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('호날두', 36, '토리노')

# 키워드 인수를 사용하면 순서를 지키지 않고 값을 넣어도 가능하다.
personal_info(age=28, address='맨체스터', name='김덕배')

# 딕셔너리의 언패킹은 **이다.
# 함수(**딕셔너리)
# 키-값 형태로 값이 저장되어 있기 때문에 *를 한 번만 사용하면 키를 사용한다는 뜻으로 됨.
# 따라서 *를 두 번 사용하여 값을 사용하도록 하자.
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 한남동'}
personal_info(**x)

# 키워드 인수를 사용하는 가변 인수 함수 만들기
def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
personal_info(name='김덕배', age=28, address='맨체스터')
personal_info(name='김덕배')

# 매개변수에 초깃값 지정하는 것도 가능하다.
'''
def 함수이름(매개변수=값):
    코드
'''

# 재귀호출
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(7))
