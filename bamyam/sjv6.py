def show_menu(): # 메뉴추가
# 입력데이터 선언
# 프로그램 메뉴출력을 위한 변수 선언
      main_menu = '''
--------------------
성적처리 프로그램 v6
--------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
--------------------
'''
      return main_menu



def add_data():
# 데이터 추가
      print('성적데이터 추가')
      name = input('이름은 ?')
      kor = int(input('국어는 ?'))
      eng = int(input('영어는 ?'))
      mat = int(input('수학은 ?'))
      tot = kor + eng + mat
      avg = tot / 3
      grd = '수' if avg >= 90 else \
      '우' if avg >= 80 else \
      '미' if avg >= 70 else \
      '양' if avg >= 60 else '가'
      with open('sungjuk.csv', 'a', encoding='utf-8') as f:
           f.write(f'{name},{kor},{eng},{mat},{tot},{avg},{grd}')



def checkData():
      print('성적데이터 조회')
      with open('sungjuk.csv', encoding='utf-8') as f:
            sjs = f.readlines()
      for sj in sjs:
            item = sj.split(',')
            row = f"이름 : {item[0]}, 국어 : {item[1]}, 영어 : {item[2]}, 수학 : {item[3]}"
            print(row)
def checkInDepth():
      print('성적데이터 상세조회')
      with open('sungjuk.csv', encoding='utf-8') as f:
            sjs = f.readlines()
      for sj in sjs:
            item = sj.split(',')
            row = (f"이름 : {item[0]}, 국어 : {item[1]}, 영어 : {item[2]}, 수학 : {item[3]}"
                   f"총점 : {item[4]}, 평균 : {item[5]}, 학점 : {item[6]}")
            print(row)

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


