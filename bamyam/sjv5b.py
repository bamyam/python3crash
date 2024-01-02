def show_menu(): # 메뉴추가
# 입력데이터 선언
# 프로그램 메뉴출력을 위한 변수 선언
      datas = {'response' : {'body' : {'totalCount' : 999, 'items' : []}}}
      main_menu = '''
--------------------
성적처리 프로그램 v5b
--------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
--------------------
'''
      return datas, main_menu


def add_data(menu, datas):
# 데이터 추가
      print('성적데이터 추가')
      user = {}
      user['name'] = input('이름은 ?')
      user['kor'] = int(input('국어는 ?'))
      user['eng'] = int(input('영어는 ?'))
      user['mat'] = int(input('수학은 ?'))
      user['tot'] = user['kor'] + user['eng'] + user['mat']
      user['avg'] = user['tot'] / 3
      user['grd'] = '수' if user['avg'] >= 90 else \
      '우' if user['avg'] >= 80 else \
      '미' if user['avg'] >= 70 else \
      '양' if user['avg'] >= 60 else '가'
      datas['response']['body']['items'].append(user)

def checkData(datas):
      print('성적데이터 조회')
      for sjs in datas['response']['body']['items']:
            print(f"이름 : {sjs['name']:s}, 국어 : {sjs['kor']:d}, 영어 : {sjs['eng']:d}, 수학 : {sjs['mat']:d}")
def checkInDepth(datas):
      print('성적데이터 상세조회')
      for data in datas['response']['body']['items']:
            print(f"이름 : {data['name']:s}, 국어 : {data['kor']:d}, 영어 : {data['eng']:d}, 수학 : {data['mat']:d}")
            print(f"총점 : {data['tot']}, 평균 : {data['avg']:.2f}, 학점 : {data['grd']}")
            print()

def menuSelect():
# 프로그램 주 실행부
      datas, main_menu = show_menu()
      print(main_menu, end = '')
      while True:
            menu = input("=> 메뉴를 선택하세요 : ")
            if menu == '1':
                  add_data(menu, datas)
            elif menu == '2':
                  checkData(datas)
            elif menu == '3':
                  checkInDepth(datas)
            elif menu == '4':
                  print('성적데이터 수정')
            elif menu == '5':
                  print('성적데이터 삭제')
            elif menu == '0':
                  print('프로그램 종료!')
                  break
            else:
                  print('잘못된 입력입니다')


