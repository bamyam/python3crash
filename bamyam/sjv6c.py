import sys
from collections import OrderedDict
import json

sjs = {'response' : {'body' : {'totalCount' : 0, 'sungjuks' : []}}}

def load_sungjuk():
    global sjs
    try :       # 만약 작업 중에 오류가 발생하면
        with open('sungjuk.json', encoding='utf-8') as f:
            sjs = json.load(f)
    except:
        pass    # 프로그램 실행 중단없이 다음 코드 실행



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
    user = OrderedDict()
    user['name'] = input('이름은 ?')
    user['kor'] = int(input('국어는 ?'))
    user['eng'] = int(input('영어는 ?'))
    user['mat'] = int(input('수학은 ?'))
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
    sjs['response']['body']['sungjuks'].append(sj)
    sjs['response']['body']['totalCount'] += 1
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
    for sj in sjs['response']['body']['sungjuks']:
        print(f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}")


def showone_sungjuk():
    print('성적데이터 상세조회')
    for sj in sjs['response']['body']['sungjuks']:
        row = (f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}"
               f"총점 : {sj['tot']}, 평균 : {sj['avg']}, 학점 : {sj['grd']}")
        print(row)


def modify_sungjuk():
    print('성적데이터 수정')


def remove_sungjuk():
    print('성적데이터 제거')


def exit_program():
    print('프로그램을 종료합니다')
    sys.exit(0)