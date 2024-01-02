# 성적 프로그램 v5
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 학점 기준 : 수우미양가
# 성적 입력, 조회, 상세조회, 수정, 삭제기능 구현
# 각 기능은 메뉴식으로 구현함 - 기능별 메뉴 선택 시 명령수행
# 성적 데이터를 dict 자료구조로 구현
# 성적 처리기능을 함수로 구현

import bamyam.sjv5b as sjv5b

def show_menu(): # 메뉴추가
# 입력데이터 선언
# 프로그램 메뉴출력을 위한 변수 선언
      datas = {'response' : {'body' : {'totalCount' : 999, 'items' : []}}}
      main_menu = '''
--------------------
성적처리 프로그램 v5
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

sjv5b.menuSelect()
#성적 데이터 입력
# for i in range(3):
#       print(f'{i+1}번째 학생데이터 입력')
#       names.append(input('이름은 ?'))
#       kors.append(int(input('국어는 ?')))
#       engs.append(int(input('영어는 ?')))
#       mats.append(int(input('수학은 ?')))

#성적처리
# for i in range(len(names)):
#       tots.append(kors[i] + engs[i] + mats[i])
#       avgs.append(tots[i] / 3)
      # if avgs[i] >= 90:
      #       grds.append('수')
      # elif avgs[i] >= 80:
      #       grds.append('우')
      # elif avgs[i] >= 70:
      #       grds.append('미')
      # elif avgs[i] >= 60:
      #       grds.append('양')
      # else :
      #       grds.append('가')
      # #다른 풀이
      # avg = avgs[len(avgs)-1]
      # grd = '수' if avg >= 90 else \
      #       '우' if avg >= 80 else \
      #       '미' if avg >= 70 else \
      #       '양' if avg >= 60 else '가'


#성적 출력
# for i in range(len(names)):
#       print(f'이름 : {names[i]:s}, 국어 : {kors[i]:d}, 영어 : {engs[i]:d}, '
#             f'수학 : {mats[i]:.1f}, 합계 : {tots[i]:d}, 평균 : {avgs[i]:.2f}, 학점 : {grds[i]}')
#
# a = '334'
# a.replace('!', '')
# print(a)
#
# for i in range(0,3):
#       print('%s님의 성적은 국어는 %d점, 영어는 %d점, 수학은 %d점으로, '
#             '총점은 %d점이며, 평균은 %d점입니다.'
#             % (names[i], kors[i], engs[i], mats[i], tots[i], int(avgs[i])
#       ))
#
# n = input()
# m = input()
# #부등호를 인식하고, 인식된 부등호대로 값을 판단하고, 0과 1을 출력
# int(2>=3)
# ('!', '>') == ('!', '>')

# print(10**1.21)
# print(10**1.0)
#
# print(1.10**2)
