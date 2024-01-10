# 도서관리 프로그램 V1
# 출력대상 : 도서명, 저자, 역자, 출판사, 출간일, 정가, 판매가, 할인율, 적립금
# bkname, author, publisher, pubdate, retail, price, saleprice, pctoff, mileage
# 도서 데이터는 데이터베이스 테이블에 저장
# 클래스 기반으로 재작성

import bamyam.BookService as bksrv

# 프로그램 주 실행부
while True:
      menu = bksrv.show_menu()
      if menu == '1': bksrv.new_book()
      elif menu == '2': bksrv.read_book()
      elif menu == '3': bksrv.readone_book()
      elif menu == '4': bksrv.modify_book()
      elif menu == '5': bksrv.remove_book()
      elif menu == '0': bksrv.exit_program()
      else: print('잘못된 입력입니다')



