# 람다 표현식
# 익명 함수를 만드는 방법으로 함수를 간단하게 작성할 수 있어
# 다른 함수의 인수로 넣을 때 주로 사용한다.
# lambda 매개변수들: 식
plus_ten = lambda x: x + 10
print(plus_ten(1))

# 람다 표현식 안에서는 변수를 만들 수 없다.
# 바깥에 있는 변수는 사용할 수 있다.
'''
다음과 같이 표현식 안에서 변수를 만들면 에러발생.
(lambda x: y = 10: x + y)(1)
'''
y = 10
print((lambda x: x + y)(1))

# def로 함수를 만들어서 map 사용하면 다음과 같다.
def plus_ten(x):
    return x + 10
list(map(plus_ten, [1, 2, 3]))

# 위 코드를 간단하게 다음과 같이 만들 수 있다.
list(map(lambda x: x + 10, [1, 2, 3]))


# 람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
# elif를 사용하면 안되고, if와 else는 세트로 들어가야한다.
# 조건이 다양할 때는 lambda보단, def로 함수를 만들고 if, elif, else를 사용하는게 가독성이 더 좋다.
a = list(range(1, 11))
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))

# map에 객체를 여러 개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b)))

# filter 사용하기
# filter(함수, 반복가능한객체)
# 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져올 때, 지정한 함수의 반환값이 True일 때만 해당 요소를 가져옴.
def f(x):
    return x > 5 and x < 10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f, a)))

print(list(filter(lambda x: x > 5 and x < 10, a)))

# reduce 사용하기
# 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수
# reduce(함수, 반복가능한객체)
def f(x, y):
    return x + y
a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(f, a))

a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(lambda x, y: x + y, a))

# 리스트(딕셔너리,세트) 표현식으로 처리할 수 있는 경우에는 map, filter와 람다 표현식 대신
# 가독성과 속도를 고려해서 그냥 리스트 표현식을 사용하자.

