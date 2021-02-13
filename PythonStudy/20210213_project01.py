# 조건문, 반복문을 공부해보자.
# 조건문에선 조건식 뒤에 :를 쓰는 것과 들여쓰기로 코드블록을 형성한다는 점에 유의하자.
x = 10
if x == 10:
    print('10 입니다')

x = int(input())
if x >= 10:
    print('10 이상입니다')
    if x == 15:
        print('15 입니다')
    if x == 20:
        print('20 입니다')


# 연습문제: if 조건문 사용하기
x = 5
if x != 10:
    print('ok')


# 심사문제: 온라인 할인 쿠폰 시스템 만들기
price = int(input())
coupon = input()

if coupon == 'Cash3000':
    print(price - 3000)

if coupon == 'Cash5000':
    print(price - 5000)


# else 사용하기
x = 5
if x == 10:
    print('10 입니다')
else:
    print('10이 아닙니다')

'''
조건부 표현식도 활용해보자
변수 = 값 if 조건문 else 값
'''

'''
파이썬 문법 중에서 False로 취급하는 것들?
- None
- False
- 0인 숫자들(진법 포함)
- 비어있는 문자열, 리스트, 튜플, 딕셔너리, 세트
- 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때
'''
if 0:
    print('true')
else:
    print('false')

if 1:
    print('true')
else:
    print('false')

if 0x1F:
    print('true')
else:
    print('false')

if 0b1000:
    print('true')
else:
    print('false')

if 13.5:
    print('true')
else:
    print('false')

if 'Hello':
    print('true')
else:
    print('false')

if '':
    print('true')
else:
    print('false')
