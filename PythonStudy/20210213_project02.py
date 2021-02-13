# 조건식을 여러 개 지정할 때
x = 10
y = 20
if x == 10 and y == 20:
    print('true')
else:
    print('false')

# 파이썬은 다음과 같은 조건문을 만들 수 있다.
if 0 < x < 20:
    print('20보다 작은 양수입니다')


# 연습문제: 합격 여부 판단하기
written_test = 75
coding_test = True
if written_test >= 80 and coding_test == True:
    print('합')
else:
    print('불')


# 국,영,수,과 네 과목 평균 점수가 80 이상일 때 합격이라 할 때 합불 판단하기
kor, eng, math, sci = map(int, input().split())
if (kor < 0 or kor > 100) or (eng < 0 or eng > 100) or (math < 0 or math > 100) or (sci < 0 or sci > 100):
    print('잘못된 점수')
else:
    avg = (kor+eng+math+sci) / 4
    if avg >= 80:
        print('합')
    else:
        print('불')


# 음료수 자판기 만들기
button = int(input())
if button == 1:
    print('코카콜라')
elif button == 2:
    print('스프라이트')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')
