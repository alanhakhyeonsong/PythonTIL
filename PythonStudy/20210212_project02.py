# 12.4 연습문제
# 딕셔너리에 게임 캐릭터 능력치 저장하기
# 체력과 이동속도가 출력되도록 만들자.

camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'])
print(camille['movement_speed'])


# 12.5 심사문제
# 딕셔너리에 게임 캐릭터 능력치 저장하기

key = input().split()
value = input().split()
player = dict(zip(key, value))
print(player)
