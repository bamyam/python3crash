import json
from collections import OrderedDict
import sys

emps = {'response' : {'body' : {'totalCount' : 0, 'employees' : []}}}


def load_employees():
    print('프로그램을 초기화합니다')
    print('프로그램이 성공적으로 초기화 되었습니다')
    global emps
    global items
    global columns


    try:
        with open('employee.json', encoding='utf-8') as f:
            emps = json.load(f)
            items = emps['response']['body']['employees']
            columns = list(emps['response']['body']['employees'][0].keys())

    except:
        pass

def show_menu():
    main_menu = '''
------------------------
사원정보 관리 프로그램v2
------------------------
1. 사원정보 저장
2. 사원정보 조회
3. 사원정보 상세조회
4. 사원정보 수정
5. 사원정보 삭제
0. 프로그램 종료
------------------------
'''
    print(main_menu)
    menu = input('원하는 메뉴를 고르시오')
    return menu


def input_employee():
    emp = OrderedDict()
    for col in columns:
        emp[col] = input(f'{col}은(는)?')
    # emp['empno'] = input('사원번호는?')
    # emp['fname'] = input('이름은?')
    # emp['lname'] = input('성은?')
    # emp['email'] = input('이메일은?')
    # emp['hdate'] = input('입사일은?')
    # emp['jobid'] = input('직책은?')
    # emp['sal'] = input('봉급은?')
    # emp['deptid'] = input('부서번호는?')
    return emp

def save_employee(emp):

    emps['response']['body']['employees'].append(emp)
    emps['response']['body']['totalCount'] += 1

    with open('employee.json', 'w', encoding='utf-8') as f:
        json.dump(emps, f, ensure_ascii=False)

def add_employee():
    print('사원정보를 등록합니다')
    emp = input_employee()
    save_employee(emp)


def read_employee():
    print('모든 사원정보를 조회합니다')
    for emp in items:
        print(f"{emp['empno']}\t{emp['fname']}\t"
              f"{emp['jobid']}\t{emp['deptid']}\n")

def readone_employee():
    print('특정 사원의 상세정보를 조회합니다')
    name = input('조회하고자 하는 사원의 이름은? ')
    for emp in items:
        if emp['fname'] == name:
            print(f"사원번호 : {emp['empno']}, 이름 : {emp['fname']}, 성 : {emp['lname']}, 이메일은 : {emp['email']}, "
                  f"입사일 : {emp['hdate']}, 직책 : {emp['jobid']}, 봉급 : {emp['sal']}, 부서번호 : {emp['deptid']}")
            break


def flush_employee():
    with open('employee.json', 'w', encoding='utf-8') as f:
        json.dump(emps, f, ensure_ascii=False)


def modify_employee():
    print('특정 사원의 정보를 수정합니다')
    # 데이터 찾기
    data = None
    idx = None
    name = input('수정하고자 하는 사원의 이름은? ')
    for i, emp in enumerate(emps['response']['body']['employees']):
        if emp['fname'] == name:
            data = emp
            idx = i
            break
    # 변경할 데이터 입력
    if data:
        user = []
        for col in columns:
            user = input(f"수정할 이메일을 입력하세요 ({data[col]})")
        # email = input(f"수정할 이메일을 입력하세요 ({data['email']})")
        # hdate = input(f"수정할 입사일을 입력하세요 ({data['hdate']})")
        # jobid = input(f"수정할 직책을 입력하세요 ({data['jobid']})")
        # sal = input(f"수정할 봉급을 입력하세요 ({data['sal']})")
        # deptid = input(f"수정할 부서번호를 입력하세요 ({data['deptid']})")


        user2=['email', 'hdate', 'jobid', 'sal', 'deptid']
        for i, j in zip(user, user2): # 데이터가 비어있으면 변경사항 없이 적용하는 기능
            if i:
                data[j] = i


    # 처리
        emps['response']['body']['employees'][idx] = data
    # 저장
        flush_employee()
    else:
        print('찾는 데이터가 없습니다')


def remove_employee():
    print('특정 사원의 정보를 제거합니다')
    data = None
    name = input('삭제하고자 하는 사원의 이름은? ')
    for emp in emps['response']['body']['employees']:
        if emp['fname'] == name:
            data = emp
            break
    if data:
        confirm = input('정말로 삭제하시겠습니까? (yes, no)')
        if confirm == 'yes':
            emps['response']['body']['employees'].remove(data)
            print(f'{name}의 데이터가 삭제되었습니다')
            emps['response']['body']['totalCount'] -= 1
            flush_employee()
        else:
             print('삭제가 취소되었습니다')
    else:
        print('삭제할 데이터가 없습니다')

def exit_employee():
    print('프로그램을 종료합니다')
    sys.exit(0)