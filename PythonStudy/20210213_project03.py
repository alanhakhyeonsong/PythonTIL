# for문을 공부해보자
for i in range(100):
    print('hello, world', i+1)

# 4부터 9까지 반복
for i in range(4, 10):
    print('hello, world', i)

# 증가폭 사용하기
for i in range(0, 10, 2):
    print('hello, world', i)

# 감소 시키기
for i in range(10, 0, -1):
    print('hello, world', i)

for i in reversed(range(10)):
    print('hello, world', i)

# 입력한 횟수대로 반복하기
count = int(input())
for i in range(count):
    print('hello, world', i)

# 시퀀스 객체로 반복하기
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'banana')
for fruit in fruits:
    print(fruit)

for letter in 'python':
    print(letter, end=' ')

for letter in reversed('python'):
    print(letter, end=' ')


# 구구단 출력하기
x = int(input())
for i in range(1, 10):
    print(x, ' * ', i, ' = ', x*i)


# while문을 공부해보자.
i = 1
while i <= 100:
    print('hello, world', i)
    i += 1

# 난수 생성해서 while문으로 반복해보기
import random

i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)


# 교통카드 잔액 출력하기
money = int(input())
while money > 1350:
    money = money - 1350
    print(money)


# 변수 두 개를 다르게 반복하기
i = 2
j = 5
while i <= 32 or j >=1:
    print(i, j)
    i *= 2
    j -= 1


# break, continue로 반복문 제어하기
i = 0
while True:
    print(i)
    i += 1
    if i == 100:
        break

for i in range(10000):
    print(i)
    if i == 100:
        break

for i in range(100):
    if i % 2 == 0:
        continue
    print(i)

i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
