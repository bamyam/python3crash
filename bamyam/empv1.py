import sys
emps = []

def load_employees():
    print('프로그램을 초기화합니다')
    print('프로그램이 성공적으로 초기화 되었습니다')
    global emps
    dicts = []

    with open('employee,csv') as f:
        datas = f.readlines()

    for data in datas:
        item = data.strip().split(',')
        d = {'empno': item[0], 'fname': item[1], 'lname': item[2], 'email': item[3],
             'hdate':item[4], 'jobid':item[5],'sal':item[6], 'deptid':item[7]}
        dicts.append(d)

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


def input_employee():
    emp = {}
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
    row = (f"{emp['empno']},{emp['fname']},{emp['lname']},"
          f"{emp['email']},{emp['hdate']},{emp['jobid']},{emp['sal']},{emp['deptid']}\n")
    with open('employee.csv', 'a', encoding='utf-8') as f:
        f.write(row)
    emps.append(row)

def add_employee():
    print('사원정보를 등록합니다')
    emp = input_employee()
    save_employee(emp)



def read_employee(emps):
    print('모든 사원정보를 조회합니다')
    result = ''
    for emp in emps:
        result += (f"{emp['empno']}\t{emp['fname']}\t"
                   f"{emp['jobid']}\t{emp['deptid']}\n")
    print(result)

def readone_employee():
    print('특정 사원의 상세정보를 조회합니다')


def modify_employee():
    print('특정 사원의 정보를 수정합니다')


def remove_employee():
    print('특정 사원의 정보를 제거합니다')


def exit_employee():
    print('프로그램을 종료합니다')
    sys.exit(0)