# 슬라이싱
# 리스트에서 필요한 부분의 아이템만 뽑아내는 것의 의미함
# 연속적인 객체들(리스트, 튜플, 문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 객체명[시작값:끝값-1:스텝]
# #시작값의 디폴트는 0, 따라서 생략하면 0부터 시작
# 끝값을 생략하면 맨 마지막까지 출력

jumin = '123456-12324567'
birth = jumin[0:6]

print(jumin, birth)

#생년월일과 -를 제외한 나머지 추출
print(jumin[7:])

# 코드에서 짝수/홀수 위치의 문자 추출
print(jumin[0::2])
print(jumin[1::2])

#역순으로 추출 : step을 -로 설정
print(jumin[14:0:-1])
print(jumin[14::-1])
print(jumin[::-1])

# 리스트 합치기 : extend, +
a = [1, 2, 3]
b = [4, 5, 6]
c = ['7', '8', '9']

a.extend(b) #a = a + b
print(a)

b.extend(c)
print(b)

# 리스트의 특정 요소 존재 파악 : in, not in
todo = ['cleaning', 'shoping', 'study', 'exercise', 'game' ]
print('drive' in todo)
print('shoping' in todo)

# 리스트의 모든 요소 존재 순회
for item in todo:
    print(item, end=', ')

# 리스트의 모든 요소 존재 순회 : enumerate
# 인덱스값도 함께 출력하기에 빅데이터 할때 좋음
for idx, item in enumerate(todo) :
    print(idx, item)

# 리스트의 모든 요소 제거 : clear
print(todo)
todo.clear()
print(todo)

# 혈액보관시스템
blood_A = []
blood_B = []
blood_AB = []
blood_O = []

for _ in range(10):
    blood = input('''
    헌혈해주셔서 감사합니다. 혈액형을 선택하세요
    A, B, AB, O :
    ''')
    if blood == 'A':
        blood_A.append(blood)
    elif blood == 'B':
        blood_B.append(blood)
    elif blood == 'AB':
        blood_AB.append(blood)
    elif blood == 'O':
        blood_O.append(blood)
#extend는 'AB'를 A, B라는 리스트로 인식해서 합침, append에 분해를 합친 느낌

print(f'''
-----------------------------
혈액형 : 개수
-----------------------------
A형 : {len(blood_A)}
B형 : {len(blood_B)}
AB형 : {len(blood_AB)}
O형 : {len(blood_O)}
-----------------------------
''')

# 혈액형 보관 시스템_선생님 풀이
bloods = []
a, b, ab, o = 0, 0, 0, 0

for idx in range(1, 10+1) :
    print('헌혈해주셔서 감사합니다. 혈액형을 선택하세요')
    blood = input('A, B, AB, O :')
    bloods.append(blood)

for bd in bloods: #bloods에 있는 값을 하나씩 꺼내서 bd에 넣고 bd의 혈액형에 따라 혈액형을 카운트함
    if bd == 'A' : a += 1
    elif bd == 'B' : b += 1
    elif bd == 'AB' : ab += 1
    elif bd == 'O' : o += 1

print(f'''
-----------------------------
혈액형 : 개수
-----------------------------
A형 : {a}
B형 : {b}
AB형 : {ab}
O형 : {o}
-----------------------------
''')

# 리스트의 항목별 빈도 계산 : count(값)
bloods.count('A')
bloods.count('B')
bloods.count('AB')
bloods.count('O')



