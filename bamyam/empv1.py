import sys
emps = []

def load_employees():
    print('프로그램을 초기화합니다')
    print('프로그램이 성공적으로 초기화 되었습니다')


def show_menu():
    main_menu = '''
---------------------
사원정보 관리 프로그램
---------------------
1. 사원정보 저장
2. 사원정보 조회
3. 사원정보 상세조회
4. 사원정보 수정
5. 사원정보 삭제
6. 프로그램 종료
---------------------
'''
    print(main_menu)
    menu = input('원하는 메뉴를 고르시오')
    return menu


def add_employee():
    print('사원정보를 등록합니다')


def read_employee():
    print('모든 사원정보를 조회합니다')


def readone_employee():
    print('특정 사원의 상세정보를 조회합니다')


def modify_employee():
    print('특정 사원의 정보를 수정합니다')


def remove_employee():
    print('특정 사원의 정보를 제거합니다')


def exit_employee():
    print('프로그램을 종료합니다')
    sys.exit(0)