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
def new_book():
    """
    도서 데이터 추가(입력 -> 처리 -> 저장)\n
    입력함수에서 데이터를 user에 받고, 처리함수에서 데이터를 user에 더 추가하고
    저장함수에서 user를 받아 저장함
    :return:
    """
    print('도서데이터 추가')
    pass


# 도서 데이터 저장(book 테이블)


def read_book():
    """
    모든 학생의 일부분의 도서 데이터 출력(번호/도서명/저자/출판사/판매가)
    :return:
    """
    pass

# 특정 학생의 모든 도서 데이터 출력
def readone_book():
    """
    특정 학생의 모든 도서 데이터 출력
    :return:
    """
    print('도서데이터 상세조회')
    bkno = input('상세 조회할 도서명은?')
    pass

# 도서 데이터 수정/삭제 시 변경사항을 파일에 반영
#  도서 데이터 수정
def modify_book():
    """
    도서 데이터 수정
    :return: 없음
    """
    print('도서데이터 수정')
    bkno = input('수정할 도서번호는?')
    pass



# 도서 데이터 삭제
def remove_book():
    """
    도서 데이터 삭제
    :param 없음:
    :return: 없음
    """
    print('도서데이터 제거')
    bkno = input('삭제할 도서번호는?')


# 프로그램 종료
def exit_program():
    """
    book program exit
    :return: None
    """
    print('프로그램을 종료합니다')
    sys.exit(0)