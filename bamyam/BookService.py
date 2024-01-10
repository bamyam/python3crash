import sys
from collections import OrderedDict
import pymysql
from bamyam.Book import Book
from bamyam.BookDAO import BookDAO
# from 모듈(디렉터리나 파일) import 클래스명(또는 함수명)

# 메뉴 출력
def show_menu():
    """
    메뉴 출력하기
    :return:
    """
    main_menu = '''
--------------------
도서관리 프로그램 v1
--------------------
1. 도서 데이터 추가
2. 도서 데이터 조회
3. 도서 데이터 상세조회
4. 도서 데이터 수정
5. 도서 데이터 삭제
0. 프로그램 종료
--------------------
'''
    print(main_menu)
    menu = input("=> 메뉴를 선택하세요 : ")
    return menu


# 도서 데이터 추가(입력 -> 처리 -> 저장)
def input_book():
    bkname = input('도서명 : ')
    author = input('저자 : ')
    publisher = input('출판사 : ')
    pubdate = input('출간일 : ')
    retail = int(input('정가 : '))
    pctoff = int(input('할인율 : '))

    bk = Book(bkname, author, publisher, pubdate, retail, pctoff)
    bk.price = bk.retail * (1-(bk.pctoff/100))
    bk.mileage = bk.retail * (bk.pctoff/100)

    return bk


def new_book():
    """
    도서 데이터 추가(입력 -> 처리 -> 저장)\n
    입력함수에서 데이터를 user에 받고, 처리함수에서 데이터를 user에 더 추가하고
    저장함수에서 user를 받아 저장함
    :return:
    """
    print('도서데이터 추가')
    bk = input_book()
    print(bk)

    rowcnt = BookDAO.insert_book(bk)
    print(f'{rowcnt} 건의 성적 데이터가 추가되었습니다')


def read_book():
    """
    모든 책의 일부분의 도서 데이터 출력(번호/도서명/저자/출판사/판매가)
    :return:
    """
    print('모든 도서 데이터 출력')
    rows = BookDAO.select_book()
    result = ''
    for row in rows:
        result += f'도서번호 : {row[0]}, 도서명 : {row[1]}, 저자 : {row[2]}, 출판사 : {row[3]}, 판매가 : {row[4]:,}\n'
    print(result)

# 특정 학생의 모든 도서 데이터 출력
def readone_book():
    """
    특정 학생의 모든 도서 데이터 출력
    :return:
    """
    print('도서데이터 상세조회')
    bkname = input('상세 조회할 도서명은?')

    row = BookDAO.selectone_book(bkname)

    if row:
        print(f'도서번호 : {row[0]}, 도서명 : {row[1]}, 저자 : {row[2]}, 출판사 : {row[3]}, 출간일 : {row[4]}\n'
              f'정가 : {row[5]:,}, 판매가 : {row[6]:,}, 할인율 : {row[7]}%, 마일리지 : {row[8]:,}, 등록일 : {row[9]}')
    else:
        print('데이터가 없어요')


def reinput_book(obk):
    bkname = input(f'도서명 ({obk[1]}): ')
    author = input(f'저자 ({obk[2]}): ')
    publisher = input(f'출판사 ({obk[3]}): ')
    pubdate = input(f'출간일 ({obk[4]}): ')
    retail = int(input(f'정가 ({obk[5]}): '))
    pctoff = int(input(f'할인율 ({obk[7]}): '))

    bk = Book(bkname, author, publisher, pubdate, retail, pctoff)
    bk.price = bk.retail * (1-(bk.pctoff/100))
    bk.mileage = bk.retail * (bk.pctoff/100)
    bk.bkno = obk[0]

    return bk


# 도서 데이터 수정/삭제 시 변경사항을 파일에 반영
#  도서 데이터 수정
def modify_book():
    """
    도서 데이터 수정
    :return: 없음
    """
    print('도서데이터 수정')
    bkname = input('수정할 도서 이름은?')
    row = BookDAO.selectone_book(bkname)


    if row:
        bk = reinput_book(row)
        rowcnt = BookDAO.update_book(bk)
        print(f'{rowcnt} 건의 도서데이터 수정됨')

    else:
        print('수정할 데이터가 없습니다')


# 도서 데이터 삭제
def remove_book():
    """
    도서 데이터 삭제
    :param 없음:
    :return: 없음
    """
    print('도서데이터 제거')
    bkno = input('삭제할 도서번호는?')
    rowcnt = BookDAO.delete_book(bkno)
    print(f'{rowcnt} 건의 도서데이터 삭제됨')


# 프로그램 종료
def exit_program():
    """
    book program exit
    :return: None
    """
    print('프로그램을 종료합니다')
    sys.exit(0)