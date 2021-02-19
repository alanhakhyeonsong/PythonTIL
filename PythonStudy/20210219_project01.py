# 딕셔너리 응용하기

# 딕셔너리에 키-값 쌍 추가하기
# setdefault: 키-값 쌍 추가 (수정은 불가)
# update: 키의 값 수정, 키가 없으면 키-값 쌍 추가
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)

x.setdefault('f', 200)
print(x)

x.update(e=333, a=90)
print(x)

# 만약 키가 숫자인 경우, update(딕셔너리) 처럼 값 수정 가능
a = {1: 'one', 2: 'two'}
a.update({1: 'ONE', 3: 'THREE'})
print(a)

# update(리스트), update(튜플): [[키, 값], [키, 값]] 형식으로 리스트(튜플)로 만들고
# 이를 다시 리스트 안에 넣어서 키-값 쌍을 나열
a.update([[2, 'TWO'],[4, 'FOUR']])
print(a)

# update(반복가능한객체): 키-값 쌍으로 된 반복 가능한 객체로 값을 수정
# 다음과 같이 zip을 사용하여 수정한다
a.update(zip([1, 2], ['one', 'two']))
print(a)

# pop(키): 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤에 삭제한 값을 반환
# pop(키, 기본값): 키가 있으면 pop처럼 반환, 없으면 기본값만 반환
# del로 []에 키를 지정하여 삭제 가능
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('a'))
print(x)

del x['d']
print(x)

# popitem(): 마지막 키-값 쌍을 삭제하여 튜플로 반환(python 3.6 이상) // 3.5ver 이하일 땐 임의로 삭제
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.popitem())

# clear(): 딕셔너리의 모든 키-값 쌍 삭제
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear()
print(x)

# get(키): 딕셔너리에서 키의 값 가져오기
# 기본값을 지정하면 해당 키가 없을 때 기본값을 반환함
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('c'))

# items(): 키-값 쌍을 모두 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())

# keys(): 키를 모두 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.keys())

# values(): 값을 모두 가져옴
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.values())

# dict.fromkeys(키리스트): 리스트(튜플)로 딕셔너리 만들기
# dict.fromkeys(키리스트, 값): 해당 값이 키의 값으로 지정됨
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys, 100)
print(y)

# 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
# 키만 출력할 땐 items, 값만 출력할 땐 values를 적절하게 사용하면 된다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)

# 딕셔너리 표현식 사용하기
# {키: 값 for 키, 값 in 딕셔너리}
# dict({키: 값 for 키, 값 in 딕셔너리)}
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

# 키와 값의 자리를 바꾸기
print({value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()})

# if 조건문을 사용하여 딕셔너리의 특정 값을 삭제시키며 출력할 수 있다.
# 이 방법은 직접 삭제하는 방식이 아니라 삭제할 대상을 제외하고 남은 쌍으로 새로 딕셔너리를 만드는 방식이다.
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)

# 중첩 딕셔너리 사용하기
# json 파일같은 구조를 만들 수 있다.
# 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}
worldclass_football_player = {
    'Sergio_Ramos': {
        'nationality': 'ESP',
        'club': 'REAL_MADRID',
        'position': 'DF',
        'b_day': '1986-03-30'
        },
    'Lionel_Messi': {
        'nationality': 'ARG',
        'club': 'FC_BARCELONA',
        'position': 'FW',
        'b_day': '1987-06-24'
        },
    'Cristiano_Ronaldo': {
        'nationality': 'POR',
        'club': 'JUVENTUS_FC',
        'position': 'FW',
        'b_day': '1985-02-05'
        },
    'Robert_Lewandowski': {
        'nationality': 'POL',
        'club': 'FC_BAYERN_MUNICH',
        'position': 'FW',
        'b_day': '1988-08-21'
        }
    }
print(worldclass_football_player['Sergio_Ramos']['club'])
print(worldclass_football_player)
