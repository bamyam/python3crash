# 파일읽기 : 파일 내 데이터 읽어오기
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# r(읽기, 생략가능), t(텍스트파일 읽기), b(바이너리파일 읽기)

# 파일읽을때 사용가능 함수
# read    : 텍스트파일의 내용을 모두 읽음
# readline : 텍스트파일의 내용을 한줄씩 읽어옴 (반복문사용)
# readlines : 텍스트파일의 내용을 한줄씩 모두 읽어옴

# 간단한 인삿말을 파일에서 읽어오기
f = open('hello.data')
doc = f.read()
f.close()
print(doc)

# 인코딩이 맞지 않으면 안 불러짐
with open('Hello2.data', encoding='UTF-8') as f:
    doc = f.read()
print(doc)

# 여러 건의 회원정보가 저장된 파일 읽어오기 1
with open('member.data') as f:
    doc1 = f.read() # 모두 읽기
print(doc1)

# 여러 건의 회원정보가 저장된 파일 읽어오기 2 (추천)
with open('member.data') as f:
    doc2 = f.readlines() # 행 단위로 모두 읽기
print(doc2) #읽은 결과는 리스트로 저장

for doc in doc2:
    print(doc)

# 여러 건의 회원정보가 저장된 파일 읽어오기 3
with open('member.data') as f:
    doc3 = f.readline() # 한 행만 읽기
print(doc3) # 한건만 출력

# 여러 건의 회원정보가 저장된 파일 읽어오기 4
docs = []
with open('member.data') as f:
    while True:
        line = f.readline() # 한 행을 읽고
        if not line: break # 읽을 내용이 없으면 중단
        docs.append(line)
print(docs)

# 여러 건의 회원정보가 저장된 파일 읽어오기 5
with open('member.data') as f:
    doc5 = f.readlines()
print(doc5)

for doc in doc5:
    item = doc.split('/')   # split(구분자)
    # 각 행의 자료를 구분자로 분리해서 리스트에 저장
    row = f'{item[0]} {item[2]} {item[3]}'
    print(row, end='') # 행의 끝에 줄바꿈이 있으므로 end='' 사용

# 앞 예제에서 파일로 저장한 성적데이터를
# 다음과 같은 형태로 화면에 출력
# 이름 : abc, 국어 : 99, 영어 : 87, 수학 : 66
with open('sungjuk.csv', encoding='utf-8') as f:
    doc6 = f.readlines()

for doc in doc6:
    item = doc.split(',')
    row = f'이름 : {item[0]}, 국어 : {item[1]}, 수학 : {item[2]}, 영어 : {item[3]}'
    print(row, end='')


