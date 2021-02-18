# 문자열 응용하기
# replace('바꿀문자열', '새문자열'): 문자열 바꾸기
s = 'Hello, world!'
s = s.replace('world', 'Python')
print(s)

# 문자 바꾸기
# translate(): 문자열 안의 문자를 다른 문자로 바꾸기
# 먼저 str.maketrans('바꿀문자','새문자') 로 변환 테이블을 만든 뒤,
# translate(테이블) 을 사용하면 결과가 변환된다.
table = str.maketrans('aeiou', '12345') # aeiou는 각각 12345에 대응한다는 의미
print('adeifdpple'.translate(table))

# 문자열 분리하기
# split(): 공백을 기준으로 문자열을 분리하여 리스트로 만든다.
# split('기준문자열')
s = 'messi ronaldo embbape debruyne sonheungmin neymar'.split()
print(s)

# 문자열 리스트를 다시 연결해보자
# ' '(공백)에 join을 사용하여 각 문자열 사이에 공백이 들어가도록 만들 수 있음
print(' '.join(s))

# upper(): 소문자->대문자 변환
# lower(): 대문자->소문자 변환
print('sonheungmin'.upper())
print('SONHEUNGMIN'.upper())

# lstrip(): 왼쪽 공백 삭제하기
# rstrip(): 오른쪽 공백 삭제하기
# strip(): 양쪽 공백 삭제하기
# 이 메소드들의 인자 안에 '삭제할문자들' 과 같이 넣으면 특정 문자를 삭제시킨다.
print('    Neymar    '.lstrip())
print('    Neymar    '.strip())

# ljust(길이): 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하고 남는 공간을 공백으로 채우기
# rjust(길이): ljust의 오른쪽 버전
print('    Neymar    '.ljust(10))

# center(길이): 문자열을 지정된 길이로 만든 뒤 가운데로 정렬하고 남는 공간을 공백으로 채우기
print('    Neymar    '.center(20))

# zfill(길이): 지정된 길이에 맞춰서 문자열 왼쪽에 0 채우기
print('35'.zfill(4))

# find('찾을문자열'): 문자열 위치 찾기
# 없으면 -1을 반환
# 중복되면 왼쪽부터 처음 찾은 곳의 인덱스 반환
print('apple pineapple'.find('pl'))

# count('문자열'): 문자열 개수 세기
# 현재 문자열에서 특정 문자열이 몇 번 나오는지 확인
print('apple pineapple'.count('pl'))
