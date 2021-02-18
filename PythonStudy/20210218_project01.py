# 2차원 리스트
# 다른 언어에서의 2차원 배열이라고 생각하면 된다.
# 리스트 = [[값, 값],[값, 값],[값, 값]]
# 요소에 접근하기는 다음과 같다.
# 리스트[세로인덱스][가로인덱스] = 값
a = [[10, 20],
     [30, 40],
     [50, 60]]
print(a[0][1])

# for 문을 한 번만 사용하여 출력하기
a = [[10, 20],
     [30, 40],
     [50, 60]]
for x, y in a: # 리스트의 가로 한 줄에서 요소 두 개를 꺼냄
    print(x, y)

# for 문을 두 번 사용하여 출력하기
a = [[10, 20],
     [30, 40],
     [50, 60]]
for i in a:     # a에서 안쪽 리스트를 꺼냄
    for j in i: # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()

# for와 range를 사용하여 출력하기
a = [[10, 20],
     [30, 40],
     [50, 60]]
for i in range(len(a)):        # 세로 크기
    for j in range(len(a[i])): # 가로 크기
        print(a[i][j], end=' ')
    print()

# while 문을 한 번만 사용하여 출력하기
a = [[10, 20],
     [30, 40],
     [50, 60]]
i = 0
while i < len(a): # 리스트의 크기(세로 크기)
    x, y = a[i]   # 요소 두 개를 한번에 가져오기
    print(x, y)
    i += 1

# while 문을 두 번 사용하여 출력하기
a = [[10, 20],
     [30, 40],
     [50, 60]]
i = 0
while i < len(a):        # 세로 크기
    j = 0
    while j < len(a[i]): # 가로 크기
        print(a[i][j], end=' ')
        j += 1           # 가로 인덱스 증가
    print()
    i += 1               # 세로 인덱스 증가

# 반복문으로 리스트 만들기
# 1차원 리스트
a = []
for i in range(10):
    a.append(0)
print(a)

# 2차원 리스트
a = []             # 빈 리스트 생성
for i in range(3):
    line = []      # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0) # 안쪽 리스트에 0 추가
    a.append(line)     # 전체 리스트에 안쪽 리스트를 추가
print(a)

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)
