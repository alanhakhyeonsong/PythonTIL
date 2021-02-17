# 튜플 응용하기

# 튜플에서 특정 값의 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

# 특정 값의 개수 구하기
a = (10, 20, 30, 15, 30, 40)
print(a.count(30))

# for 반복문으로 요소 출력하기
a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end=' ')
print()

# 튜플 표현식 사용하기
# tuple(식 for 변수 in 리스트 if 조건식)
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

# tuple에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

# 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))
