# 집합을 표현하는 세트 사용하기

# 세트 만들기
# 세트 = {값1, 값2, 값3}
# 세트에 들어가는 요소는 중복 불가
# 세트는 순서가 정해져 있지 않기 때문에, 매번 출력시 순서가 다르게 나온다.
# 다른 시퀀스 자료형과 달리 특정 요소만 출력할 수는 없다.
realmadrid = {'sergio_ramos', 'karim_benzema', 'eden_hazard', 'luka_modric', 'tony_kroos'}
print(realmadrid)

# 세트에 특정 값이 있는지 확인하기
# 값 in 세트
# 값 not in 세트
print('tony_kroos' in realmadrid)
print('kylian_mbappe' not in realmadrid)

# set을 사용하여 세트 만들기
# set(반복가능한객체)
# 중복되는 요소는 포함하지 않는다.
a = set('apple')
print(a)

b = set(range(5))
print(b)

c = set()
print(c)

# 집합 연산 사용하기
# 합집합
# 세트1 | 세트2
# set.union(세트1, 세트2)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))

# 교집합
# 세트1 & 세트2
# set.intersection(세트1, 세트2)
print(a & b)
print(set.intersection(a, b))

# 차집합
# 세트1-세트2
# set.difference(세트1, 세트2)
print(a - b)
print(set.difference(a, b))

# 대칭 차집합
# 세트1 ^ 세트2
# set.symmetric_difference(세트1, 세트2)
print(a ^ b)
print(set.symmetric_difference(a, b))

# 집합 연산 후 할당 연산자 사용하기
# 현재 세트에 다른 세트를 더하기
# 세트 |= 세트2
# 세트1.update(세트2)
a = {1, 2, 3, 4}
a |= {5}
print(a)

a = {1, 2, 3, 4}
a.update({5})
print(a)

# 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장
# 세트1 &= 세트2
# 세트1.intersection_update(세트2)
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
print(a)

a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
print(a)

# 현재 세트에서 다른 세트를 빼기
# 세트1 -= 세트2
# 세트1.difference_update(세트2)
a = {1, 2, 3, 4}
a -= {3}
print(a)

a = {1, 2, 3, 4}
a.difference_update({3})
print(a)

# 현재 세트와 다른 세트 중 겹치지 않는 요소만 현재 세트에 저장
# 세트1 ^= 세트2
# 세트1.symmetric_difference_update(세트2)
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
print(a)
