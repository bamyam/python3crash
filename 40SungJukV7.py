# 성적 프로그램 v6c
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 학점 기준 : 수우미양가
# 성적 입력, 조회, 상세조회, 수정, 삭제기능 구현
# 각 기능은 메뉴식으로 구현함 - 기능별 메뉴 선택 시 명령수행
# 성적 데이터는 데이터베이스 테이블에 저장
# 저장양식은 '이름, 국어, 영어, 수학, 총점, 평균, 학점' 형태로 한다


import bamyam.sjv7 as sjv7

# 프로그램 주 실행부
while True:
      menu = sjv7.show_menu()
      if menu == '1': sjv7.add_sungjuk()
      elif menu == '2': sjv7.show_sungjuk()
      elif menu == '3': sjv7.showone_sungjuk()
      elif menu == '4': sjv7.modify_sungjuk()
      elif menu == '5': sjv7.remove_sungjuk()
      elif menu == '0': sjv7.exit_program()
      else: print('잘못된 입력입니다')


