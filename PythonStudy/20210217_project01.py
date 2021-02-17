# 리스트 응용하기

# 리스트에 요소 하나 추가하기
# append: 요소 하나를 추가(맨 뒤에 추가가 됩니다)
a = [10, 20, 30]
a.append(500)
print(a)

# 빈 리스트에도 추가 가능
b = []
b.append(10)
print(b)

# 리스트 확장하기
# extend: 리스트에 요소를 여러 개 추가
# 결국은 리스트와 리스트를 연결하는 꼴과 같은 모양
a = [10, 20, 30]
a.extend([500, 600, 1052])
print(a)
print(len(a))

# insert: 리스트의 특정 인덱스에 넣기
# 첫 번째 인자는 인덱스 번호, 두 번째 인자는 요소의 값
# 인덱스 번호는 마찬가지로 0부터 시작하게 됩니다.
# insert(len(리스트), 요소): 리스트 맨 끝에 요소를 추가함
# insert(0, 요소): 리스트 맨 처음에 요소를 추가함
a = [10, 20, 30]
a.insert(2, 404)
print(a)

# 리스트의 요소 삭제하기
# pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제
# remove: 특정 값을 찾아서 삭제(단, 삭제할 값이 중복적으로 존재히면 가장 처음 찾은 값을 삭제함)
a = ["cristiano", "leo", "kdb"]
a.pop()
print(a)

a = ["cristiano", "leo", "kdb"]
a.remove("leo")
print(a)

a = [10, 20, 40, 20, 30]
a.remove(20)
print(a)

'''
결론적으로 리스트의 메소드를 적절히 사용하면 stack, queue 처럼 사용할 수 있다.
추가로 파이썬에선 queue를 좀 더 효율적으로 사용할 수 있도록 deque도 제공한다.
from collections import deque
a = deque([10, 20, 30]) // deque(반복가능한객체)
a.append(500) // 오른쪽에 추가
a.popleft() // 왼쪽 요소 하나 삭제
'''

# index(값): 리스트에서 특정 값의 인덱스 구하기
a = [10, 20, 30, 11, 192, 20]
print(a.index(192))

# count(값): 특정 값의 개수 구하기
a = [10, 20, 30, 11, 192, 20]
print(a.count(20))

# reverse(): 리스트의 순서 뒤집기
a = [10, 20, 30, 40, 50, 60]
a.reverse()
print(a)

# sort(): 리스트 정렬
# sort(reverse=True): 내림차순 정렬
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)

# clear(): 리스트 모든 요소 삭제
# del a[:]와 같은 효과
a = [10, 20 ,30]
a.clear()
print(a)

# 리스트가 비어있는지 확인하기
'''
if not seq: // 리스트가 비어 있으면 true
if seq: // 리스트에 내용이 있으면 true
'''

# 리스트의 할당과 복사
# 다음과 같이 하면 리스트 하나를 두 레퍼런스 변수가 참조하게 됩니다.
a = [0, 0, 0, 0, 0]
b = a

print(a is b) # 같은 객체이므로 true

# 리스트 a, b를 따로 만들기 위해선, copy()를 사용합니다.
a = [0, 0, 0, 0, 0]
b = a.copy

print(a is b) # 서로 다른 객체이므로 false
print(a == b) # 복사된 요소는 모두 같으므로 true

# 리스트 표현식
# [식 for 변수 in 리스트]
# list(식 for 변수 in 리스트)
# 리스트 표현식의 동작 순서는 리스트에서 숫자를 하나씩 변수로 꺼내어 이 변수를 식에 넣어 리스트 형식으로 만드는 것입니다.
a = [i + 5 for i in range(10)]
print(a)

# 마찬가지로 if 조건문도 섞어서 사용 가능합니다.
# [식 for 변수 in 리스트 if 조건식]
# list(식 for 변수 in 리스트 if 조건식)
a = [i for i in range(10) if i % 2 == 0]
print(a)

# for 반복문과 if 조건문을 여러 번 사용도 가능합니다.
# 다음 코드는 중첩 for문의 효과와 같습니다.
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

# 리스트에 map 사용하기
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
a = [1.2, 2.5, 4.6, 3.82]
a = list(map(int, a))
print(a)
