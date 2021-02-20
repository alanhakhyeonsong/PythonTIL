# 부분 집합과 상위집합 확인하기

# 현재세트 <= 다른세트  (진부분집합인지 확인은 < 연산자를 사용한다)
# 현재세트.issubset(다른세트)
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
print(a.issubset({1, 2, 3, 4, 5}))

# 상위집합임을 확인하기
# 현재세트 >= 다른세트
# 현재세트.issuperset(다른세트)
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})
print(a.issuperset({1, 2, 3, 4, 5}))

# 세트가 같은지 다른지 확인하기
# == 연산자를 사용하자
# 순서를 달리해도 상관 없다.
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})
print(a == {4, 3, 1, 2})

# 세트가 겹치지 않는지 확인하기
# 현재세트.isdisjoint(다른세트)
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))

# 세트 조작하기
# add(요소): 세트에 요소 추가
# remove(요소): 세트에서 특정 요소 삭제(없으면 에러 발생)
# discard(요소): 세트에서 특정 요소 삭제(없으면 그냥 넘어감)
a = {1, 2, 3, 4}
a.add(5)
print(a)

a.remove(3)
print(a)

a.discard(7)
print(a)

# pop(): 세트에서 임의의 요소 삭제
# clear(): 세트의 모든 요소 삭제
# len(세트): 세트의 요소 개수 구하기
a = {1, 2, 3, 4}
print(a.pop())
print(len(a))

# 세트의 할당과 복사
a = {1, 2, 3, 4}
b = a
print(a is b) # True가 나오는 이유는 변수 이름만 다르지 세트 a, b는 같은 객체이기 때문

# 완전히 다른 두 객체로 만드려면 copy 메소드를 통해 복사하자
a = {1, 2, 3, 4}
b = a.copy()
print(a is b) # 서로 다른 객체이므로 False
print(a == b)

# 세트 표현식 사용하기
# {식 for 변수 in 반복가능한객체}
# set(식 for 변수 in 반복가능한객체)
a = {i for i in 'Cristiano Ronaldo'}
print(a)

# 세트 표현식에 if 조건문 사용하기
# {식 for 변수 in 세트 if 조건식}
# set(식 for 변수 in 세트 if 조건식)
a = {i for i in 'pineapple' if i not in 'apl'}
print(a)
