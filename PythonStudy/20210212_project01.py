'''
딕셔너리 만들기
딕셔너리 = {키1: 값1, 키2: 값2}
딕셔너리는 중괄호 안에 키: 값 형식으로 저장하고 콤마로 구분한다.
키나 값에는 모든 자료형을 사용할 수 있고 섞어서도 가능하다.
(단, 키에는 리스트와 딕셔너리를 사용할 수 없음)
해시(hash) 기법을 사용하는 자료구조이고 다른 언어의 hashmap과 기능이 같다.
'''
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72}
print(lux)

# 키 이름이 중복되는 경우 중복되는 키는 저장되지 않고, 가장 뒤에 있는 값만 사용된다.
lux = {'health': 490, 'health': 800, 'mana': 334, 'melle': 550, 'armor': 18.72}
print(lux['health'])

# 빈 딕셔너리 만들기
# 딕셔너리 = {}
# 딕셔너리 = dict()
x = {}
print(x)

# dict로 딕셔너리 만들기
# 1. dict에서 키=값 형식으로 만들기
lux1 = dict(health=490, mana=800, melle=550, armor=18.72)
print(lux1)

# 2. zip 함수를 이용하여 만들기
lux2 = dict(zip(['health', 'mana', 'melle', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

# 3. 리스트 안에 (키, 값) 형식의 튜플을 나열하기
lux3 = dict([('health', 490), ('mana', 334), ('melle', 550), ('armor', 18.72)])
print(lux3)

# 4. dict 안에서 중괄호로 딕셔너리 생성하기
lux4 = dict({'health': 490, 'health': 800, 'mana': 334, 'melle': 550, 'armor': 18.72})
print(lux4)


# 딕셔너리의 키에 접근하고 값 할당하기
# 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당된다.
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72}
print(lux['health'])
lux['health'] = 2037
lux['mana'] = 1184
print(lux)

lux['mana_regen'] = 3.28
print(lux)

# 딕셔너리에 키가 있는지 확인하기
# 키 in 딕셔너리
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72}
print('attack_speed' in lux)

# 딕셔너리의 키 개수 구하기
print(len(lux))
