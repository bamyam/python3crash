import sys
from collections import OrderedDict
import json

sjs = {'response' : {'body' : {'totalCount' : 0, 'sungjuks' : []}}}
items = []
totalCount = 0



def load_sungjuk():
    global sjs
    global items
    global totalCount


    try :       # 만약 작업 중에 오류가 발생하면
        with open('sungjuk.json', encoding='utf-8') as f:
            sjs = json.load(f)
            items = sjs['response']['body']['sungjuks']
            totalCount = sjs['response']['body']['totalCount']


    except:
        items = sjs['response']['body']['sungjuks']
        totalCount = sjs['response']['body']['totalCount']    # 프로그램 실행 중단없이 다음 코드 실행

def show_menu():
    main_menu = '''
--------------------
성적처리 프로그램 v6c
--------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
--------------------
'''
    print(main_menu)
    menu = input("=> 메뉴를 선택하세요 : ")
    return menu

def read_sungjuk():
    sungjuk = input('이름과 성적을 입력하세요(예 : 홍길동 99 88 99) :')
    data = sungjuk.split() # 빈칸을 문자열로 분리할 때는 구분자를 안 넣으면 빈칸으로 인식

    user = OrderedDict()
    user['name'] = data[0]
    user['kor'] = int(data[1])
    user['eng'] = int(data[2])
    user['mat'] = int(data[3])
    return user

def compute_sungjuk(user):
    user['tot'] = user['kor'] + user['eng'] + user['mat']
    user['avg'] = float(f"{user['tot'] / 3:.1f}")
    user['grd'] = '수' if user['avg'] >= 90 else \
        '우' if user['avg'] >= 80 else \
            '미' if user['avg'] >= 70 else \
                '양' if user['avg'] >= 60 else '가'
    return user

def save_sungjuk(sj):  # 이제는 파일과 메모리의 sjs변수에 값을 저장
    # 메모리 내에 생성된 json객체에 방금 생성한 성적 데이터 저장
    # sjs['response']['body']['sungjuks'].append(sj)
    # sjs['response']['body']['totalCount'] += 1

    items.append(sj)
    sjs['response']['body']['totalCount'] += 1
    # totalCount += 1

    # 메모리 내에 생성된 json객체를 파일에 저장
    with open('sungjuk.json', 'w', encoding='utf-8') as f:
        json.dump(sjs, f, ensure_ascii=False)
    # 메모리에 존재하는 sjs변수ㅜ에도 파일에 추가된 성적데이터 반영


def add_sungjuk():
    print('성적데이터 추가')
    user = read_sungjuk()
    compute_sungjuk(user)
    save_sungjuk(user)

def show_sungjuk():
    print('성적데이터 조회')
    for sj in items:
        print(f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}")


def showone_sungjuk():
    print('성적데이터 상세조회')
    name = input('상세 조회할 학생 이름은?')
    info = '찾는 데이터가 없습니다'
    for sj in items:
        if sj['name'] == name :
            info = f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']} "\
                   f"총점 : {sj['tot']}, 평균 : {sj['avg']}, 학점 : {sj['grd']}"
            break
    print(info)

def read_again(data, name):
    kor = int(input(f"새로운 국어는? ({data['kor']})"))
    eng = int(input(f"새로운 영어는? ({data['eng']})"))
    mat = int(input(f"새로운 수학은? ({data['mat']})"))

    data = OrderedDict()
    data['name'] = name
    data['kor'] = kor
    data['eng'] = eng
    data['mat'] = mat

    return data


def flush_sungjuk():
    with open('sungjuk.json', 'w', encoding='utf-8') as f:
        json.dump(sjs, f, ensure_ascii=False)


def modify_sungjuk():
    print('성적데이터 수정')
    name = input('수정할 학생 이름은?')
    # 수정할 학생 데이터 찾기
    data = None
    idx = None
    for i, sj in enumerate(items) :
        if sj['name'] == name:
            data = sj
            idx = i

    # data = None
    # idx = 0
    # for sj in items:
    #     if sj['name'] == name:
    #         data = sj
    #     idx += 1


    # 수정할 학생 데이터를 찾았다면
    # 새로운 값을 입력받고, 다시 성적 처리함
    if data:
        data = read_again(data, name)

        compute_sungjuk(data)

        # 기존 데이터를 버리고 새로운 데이터로 재설정
        items[idx] = data

        # 변경사항을 json 파일에 반영
        flush_sungjuk()

    else:
        print('찾는 데이터가 없습니다!')

def remove_sungjuk():
    print('성적데이터 제거')


def exit_program():
    print('프로그램을 종료합니다')
    sys.exit(0)