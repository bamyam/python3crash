# 딕서너리
# 이름key과 값value으로 구성된 연관배열(associate array)의 일종
# 자료구조 만들때 {}(중괄호)를 사용하고
# 이름과 값은 : 으로 구분해서 정의하고 쉼표를 이용해서 데이터를 구분함
# 예시 : ages = {'박찬호' : 40, '박찬승' : 42}
# 다른 언어의 JSON과 유사한 구조
# 데이터분석시 주로 사용하는 자료구조 : mongodb
# 키를 통해 자료를 찾는 해쉬테이블을 이용하므로 검색속도가 빠름
# 리스트는 인덱스로 값을 참조하지만, 딕셔너리는 키로 값을 참조함
# 키는 중복불가이지만 값은 중복가능

mids = {'C/C++': 'A', 'Java': 'B+', '네트워킹': 'C', '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
print(mids)
print(mids.keys())

# 회원정보를 dict로 선언
# key : 이름, 아이디, 비번, 이메일, 주소, 성적(국영수)

member = {'이름': '서승재', '아이디': 'bamyam', '비번': '12345', '이메일': 'bamy@namver.c',
          '주소': '서울시 관악구', '성적': [80, 90, 40]}
print(member['이름'])

# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명.get(키)
print(member['이름'])
print(member['아이디'])
print(member['성적'][0])

print(member.get('성적'))
print(member.get('이름'))

# 존재하지 않는 키를 지정시
member['zipcode']  # 오류발생
member.get('zipcode') # 실행해서 None의 값을 나타내고 오류도 나타나지 않음

# 새로운 항목 추가 : 변수명[새로운키] = 새로운 값
member['zipcode'] = '1,2,3,4,5'
print(member)

# 기존 항목 변경 : 변수명[키] = 변경할값
member['zipcode'] = '98459'
member['addr'] = '서울시 광진구'

print(member)

# 기존 항목 삭제 : del 변수명[키], 변수명.pop(키)
del member['zipcode']
member.pop('addr')

print(member)

# 존재하지 않는 키 삭제
del member['blood']       # 오류 발생
member.pop('blood')       # 오류 발생
member.pop('blood', None) # None

# 항목수 조회
print(len(member))

# dict의 모든 키/값 조회 : keys, values
print(member.keys()) # 인덱스 조회 불가 및 깔끔하게 안 보임
print(member.values())
print(list(member.keys())) # 리스트에 넣어서 보면 깔끔하게 보이고 인덱스 조회 가능
print(member.values())

# dict 전체 항목 출력
# 출력형식은 '키 = 값'
for key in member.keys():
    print(f'{key} = {member[key]}')

for key, value in zip(member.keys(), member.values()):
    print(f'{key} = {value}')

# 중간고사 성적 관리 프로그램
# 성적저장 하는 딕셔너리
mids = {'C/C++': 'A', 'Java': 'B+', '모바일': 'C', '보안': 'A+', '해킹': 'F', '시스템': 'C+'}
# 2 성적조회
print(mids['Java'], mids['시스템'])
#3 성적삽입
mids['파이썬'] = 'A'
mids['OS'] = 'A+'
print(mids)
#4 성적 수정
mids['Java'] = 'F'
mids['시스템'] = 'A'
print(mids)
# 전체 성적표 출력하기
print('''
--------------------------------
             성적표
--------------------------------''')
for key in mids.keys():
    print(f'|{key:>10s}    |       {mids[key]}')
    print('-------------------------------') # 제대로 정렬하는 방법

# 수학시험 프로그램
quests = {'3+2': 3, '5÷2의 몫': 5, '10-2': 3, '10^2 x 2': 5, '1-(10÷4의 나머지)': 5, '2^4': 3, '4÷2': 3}
answers = (5, 2, 8, 200, -1, 16, 2)
cnt = 0
wrong = 0
score = 0
for idx, quest in enumerate(quests.keys()):
    print(idx, quest)
    print(f'문제 : {quest}')
    answer = int(input('정답을 입력하세요'))
    if answer == answers[idx]:
        cnt += 1
        score += quests[quest]
    else :
        wrong += 1

print(f'''----------------------
정답 개수 :    {cnt}
오답 개수 :    {wrong}
Total Score : {score}
----------------------''')

# 수학시험 프로그램_선생님 풀이
# 투플 안에 투플을 넣는 방법
quizs = (('3 + 2는 ? (3점)', 5, 3), ('5 ÷ 2의 몫은? (5점)', 2, 5),
         ('10-2는? (3점)', 8, 3), ('10^2 x 2는? (5점)', 200, 5), ('1-(10÷4의 나머지는)? (5점)', -1, 5),
         ('2의 4제곱은? (3점)', 16, 3), ('4 ÷ 2는? (3점)', 2, 3))
trueCount = 0
falseCount = 0
totalScore = 0

for idx, q in enumerate(quizs) :
    print(f'문제 {idx+1}/7 : ', q[0])
    answer = int(input('정답을 입력하세요 :'))
    if answer == q[1]:
        trueCount += 1
        totalScore += q[2]
    else: falseCount += 1

print(f'''
-----------------
정답 개수 : {trueCount}
오답 개수 : {falseCount}
총 점수 : {totalScore}
-----------------
''')


# 회원가입 프로그램
# 시작할 때 선택유도
start = int(input('1. 회원가입, 2. 프로그램 종료'))
infor = {}
# 1과 2입력 에 따른 다른 절차
while True :
    if start == 1:
        id = input('아이디를 입력하세요')
        passwd = input('비밀번호를 입력하세요')
        infor[id] = passwd
        start = int(input('1. 회원가입, 2. 프로그램 종료'))
    elif start == 2:
        break
    else :
        print('잘못된 입력입니다, 다시 선택해주세요')
        start = input('1. 회원가입, 2. 프로그램 종료')

print(f'''-------------------------
아이디 : 비밀번호
-------------------------''')
for i in infor.keys():
    print(f'{i} : {infor[i]}')
print('-------------------------')

# 회원가입 프로그램_선생님 풀이_v2
users = {}
while True:
    menu = input('1. 회원가입, 2. 프로그램 종료')
    if menu == '1':
        userid = input('아이디를 입력하세요. ')
        passwd = input('비밀번호를 입력하세요. ')
        users[userid] = passwd
    elif menu == '2':
        print('--------------------')
        print('아이디 : 비밀번호')
        print('--------------------')
        for k in users.keys():
            print(f'{k} : {users[k]}')
        print('--------------------')
        break
    else:
        print('잘못된 입력입니다!')
        continue

# 회원가입 프로그램_선생님 풀이_v2
# 현업에서는 json처럼 메타데이터를 포함시키기 위해 딕셔너리를 다르게 씀
users = {'response' : {'body' : {'totalCount' : 999, 'items' : []}}}
print(users['response'])
print(users['response']['body'])
print(users['response']['body']['items'])

print(users['response']['body']['items'].append({'uid':'abc', 'pwd':'123'}))
print(users['response']['body']['items'].append({'uid':'xyz', 'pwd':'987'}))

for item in users['response']['body']['items']:
    for key in item.keys():
        print(key, item[key])

while True:
    menu = input('1. 회원가입, 2. 프로그램 종료')
    if menu == '1':
        userid = input('아이디를 입력하세요. ')
        passwd = input('비밀번호를 입력하세요. ')
        user = {}
        user['userid'] = userid
        user['passwd'] = passwd
        users['response']['body']['items'].append(user)
    elif menu == '2':
        print('--------------------')
        print('아이디 : 비밀번호')
        print('--------------------')
        for item in users['response']['body']['items']:
            for k in item.keys():
                print(f'{k} : {item[k]}')
        print('--------------------')
        break
    else:
        print('잘못된 입력입니다!')
        continue




