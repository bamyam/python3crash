import json
from collections import OrderedDict
import sys

emps = {'response' : {'body' : {'totalCount' : 0, 'employees' : []}}}


def load_employees():
    print('프로그램을 초기화합니다')
    print('프로그램이 성공적으로 초기화 되었습니다')
    global emps


    try:
        with open('employee.json', encoding='utf-8') as f:
            emps = json.load(f)

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
    emp['empno'] = input('사원번호는?')
    emp['fname'] = input('이름은?')
    emp['lname'] = input('성은?')
    emp['email'] = input('이메일은?')
    emp['hdate'] = input('입사일은?')
    emp['jobid'] = input('직책은?')
    emp['sal'] = input('봉급은?')
    emp['deptid'] = input('부서번호는?')
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
    for emp in emps['response']['body']['employees']:
        print(f"{emp['empno']}\t{emp['fname']}\t"
              f"{emp['jobid']}\t{emp['deptid']}\n")

def readone_employee():
    print('특정 사원의 상세정보를 조회합니다')


def modify_employee():
    print('특정 사원의 정보를 수정합니다')


def remove_employee():
    print('특정 사원의 정보를 제거합니다')


def exit_employee():
    print('프로그램을 종료합니다')
    sys.exit(0)