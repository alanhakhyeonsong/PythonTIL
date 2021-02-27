# 변수의 사용 범위
x = 10       # 전역 변수
def foo1():
    print(x) # 전역 변수 출력

foo1()
print(x)     # 전역 변수 출력

def foo2():
    x = 10   # foo2의 지역 변수
    print(x) # foo2의 지역 변수 출력

foo2()

''' 에러 발생. foo2의 지역 변수는 출력 불가함
print(x)
'''


# 함수 안에서 전역 변수의 값 변경하기
x = 10       # 전역 변수
def foo3():
    global x # 전역 변수 x를 사용하겠다고 설정
    x = 20   # 전역 변수 값 변경
    print(x) # 전역 변수 출력

foo3()
print(x)     # 전역 변수 출력


# 함수 안에서 함수 만들기
'''
def 함수이름1():
    코드
    def 함수이름2():
        코드
'''
# 이 경우, print_hello(), print_message() 순으로 실행하게 된다.
def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()

print_hello()

# 지역 변수의 범위
def A1():
    x = 10     # A1의 지역변수 x
    def B():
        x = 20 # x에 20 할당(x는 전역 변수가 아니기 때문에 정상적으로 동작하지 않는다)
               # 이름만 같은 지역 변수 x를 새로 만드는 꼴
    B()
    print(x)   # A1의 지역 변수 x 출력

A1()

def A2():
    x = 10     # A2의 지역변수 x
    def B():
        nonlocal x # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20     # A2의 지역 변수 x에 20 할당
        
    B()
    print(x)   # A2의 지역 변수 x 출력

A2()

# 클로저: 함수를 둘러싼 환경(지역 변수, 코드)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수
# 프로그램의 흐름을 변수에 저장할 수 있는 이점이 있어서, 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용한다.
# 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용한다.
def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add
c = calc()
print(c(1), c(2), c(3), c(4), c(5))
