# 성적 데이터를 저장할 변수 선언
# [ {'name': 혜교, 'kor': 77, 'eng': 33, 'mat': 86},
#   {'name': 지현, 'kor': 66, 'eng': 44, 'mat': 54},
#   {'name': 수지, 'kor': 55, 'eng': 55, 'mat': 43} ]
sjs = []

#
def show_menu(): # 메뉴추가
# 입력데이터 선언
# 프로그램 메뉴출력을 위한 변수 선언
      main_menu = '''
--------------------
성적처리 프로그램 v6b
--------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
--------------------
'''
      print(main_menu)
      menu = input("=> 메뉴를 선택하세요 : ")
      return menu


def read_sungjuk():
      user = {}
      user['name'] = input('이름은 ?')
      user['kor'] = int(input('국어는 ?'))
      user['eng'] = int(input('영어는 ?'))
      user['mat'] = int(input('수학은 ?'))
      return user

def compute_sungjuk(user):
      user['tot'] = user['kor'] + user['eng'] + user['mat']
      user['avg'] = user['tot'] / 3
      user['grd'] = '수' if user['avg'] >= 90 else \
            '우' if user['avg'] >= 80 else \
                  '미' if user['avg'] >= 70 else \
                        '양' if user['avg'] >= 60 else '가'
      return user

def add_data():
# 데이터 추가
      print('성적데이터 추가')
      user = read_sungjuk()
      compute_sungjuk(user)
      save_sungjuk(user)

def checkData():
      print('성적데이터 조회')
      for sj in sjs:
            print(f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}")

def checkInDepth():
      print('성적데이터 상세조회')
      for sj in sjs:
            row = (f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}"
                   f"총점 : {sj['tot']}, 평균 : {sj['avg']}, 학점 : {sj['grd']}")
            print(row)

def save_sungjuk(sj): # 이제는 파일과 메모리의 sjs변수에 값을 저장
      global sjs
      with open('sungjuk.csv', 'a', encoding='utf-8') as f:
            row = (f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}"
                   f"총점 : {sj['tot']}, 평균 : {sj['tot']:.1f}, 학점 : {sj['grd']}\n")
            f.write(row)
      # 메모리에 존재하는 sjs변수ㅜ에도 파일에 추가된 성적데이터 반영
      sjs.append(sj)

def menuSelect():
# 프로그램 주 실행부
      show_menu()
      while True:
            menu = input("=> 메뉴를 선택하세요 : ")
            if menu == '1':
                  add_data()
            elif menu == '2':
                  checkData()
            elif menu == '3':
                  checkInDepth()
            elif menu == '4':
                  print('성적데이터 수정')
            elif menu == '5':
                  print('성적데이터 삭제')
            elif menu == '0':
                  print('프로그램 종료!')
                  break
            else:
                  print('잘못된 입력입니다')

# 프로그램 시작시 sungjuks.csv 파일을 읽어 sjs변수에 초기화
def load_sungjuk():
      global sjs

      with open('sungjuk.csv', encoding='utf-8') as f:
            datas = f.readlines()

      # csv 형태로 저장되어 있는 성적 데이터를 dict형태로 변환해서 메모리에 저장
      dicts = []
      for data in datas:
            item = data.strip().split(',') #strip은 각종 제어문자(줄바꿈, 공백, 탭) 제거
            d = {'name': item[0], 'kor': item[1], 'eng': item[2],
                 'mat': item[3], 'tot':item[4], 'avg':item[5] ,
                 'grd':item[6]}
            dicts.append(d)

      sjs = dicts # dict로 변환된 데이터를 sjs변수에 저장