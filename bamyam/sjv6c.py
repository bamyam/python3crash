import sys
from collections import OrderedDict
import json

sjs = {'response' : {'body' : {'totalCount' : 0, 'sungjuks' : []}}}
items = []
totalCount = 0



def load_sungjuk():
    """
    sungjuk.json에서 데이터 받기
    :return: global(sjs(전체 데이터), items(성적 데이터), totalCount(자료의 수))
    """
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

# 메뉴 출력
def show_menu():
    """
    메뉴 출력하기
    :return:
    """
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

# 성적 데이터 입력받음
def read_sungjuk():
    """
    이름과 성적 데이터(국어, 영어 수학)를
    dict형 변수인 user에 기입
    :return: user(name, kor, eng, mat)
    """
    sungjuk = input('이름과 성적을 입력하세요(예 : 홍길동 99 88 99) :')
    data = sungjuk.split() # 빈칸을 문자열로 분리할 때는 구분자를 안 넣으면 빈칸으로 인식

    user = OrderedDict()
    user['name'] = data[0]
    user['kor'] = int(data[1])
    user['eng'] = int(data[2])
    user['mat'] = int(data[3])
    return user

# 성적 처리(총점/평균/학점 계산)
def compute_sungjuk(user):
    """
    성적 처리(총점/평균/학점 계산)
    user에 담긴 성적 데이터를 처리하는 프로그램
    :param user: read_sungjuk에서 만든 성적데이터
    :return: user(name, kor, eng, mat, tot, avg, grd)
    """
    user['tot'] = user['kor'] + user['eng'] + user['mat']
    user['avg'] = float(f"{user['tot'] / 3:.1f}")
    user['grd'] = '수' if user['avg'] >= 90 else \
        '우' if user['avg'] >= 80 else \
            '미' if user['avg'] >= 70 else \
                '양' if user['avg'] >= 60 else '가'
    return user

# 성적 데이터 저장(sungjuk.json 파일)
def save_sungjuk(sj):  # 이제는 파일과 메모리의 sjs변수에 값을 저장
    # 메모리 내에 생성된 json객체에 방금 생성한 성적 데이터 저장
    """
    성적 데이터 저장(sungjuk.json 파일)
    :param sj: user(name, kor, eng, mat, tot, avg, grd)
    :return: 없음
    """
    items.append(sj)
    sjs['response']['body']['totalCount'] += 1
    # totalCount += 1

    # 메모리 내에 생성된 json객체를 파일에 저장
    with open('sungjuk.json', 'w', encoding='utf-8') as f:
        json.dump(sjs, f, ensure_ascii=False)
    # 메모리에 존재하는 sjs변수ㅜ에도 파일에 추가된 성적데이터 반영

# 성적 데이터 추가(입력 -> 처리 -> 저장)
def add_sungjuk():
    """
    성적 데이터 추가(입력 -> 처리 -> 저장)\n
    입력함수에서 데이터를 user에 받고, 처리함수에서 데이터를 user에 더 추가하고
    저장함수에서 user를 받아 저장함
    :return:
    """
    print('성적데이터 추가')
    user = read_sungjuk()
    compute_sungjuk(user)
    save_sungjuk(user)

# 모든 학생의 일부분의 성적 데이터 출력(이름/국어/영어/수학)
def show_sungjuk():
    """
    모든 학생의 일부분의 성적 데이터 출력(이름/국어/영어/수학)
    :return:
    """
    print('성적데이터 조회')
    for sj in items:
        print(f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']}")

# 특정 학생의 모든 성적 데이터 출력
def showone_sungjuk():
    """
    특정 학생의 모든 성적 데이터 출력
    :return:
    """
    print('성적데이터 상세조회')
    name = input('상세 조회할 학생 이름은?')
    info = '찾는 데이터가 없습니다'
    for sj in items:
        if sj['name'] == name :
            info = f"이름 : {sj['name']}, 국어 : {sj['kor']}, 영어 : {sj['eng']}, 수학 : {sj['mat']} "\
                   f"총점 : {sj['tot']}, 평균 : {sj['avg']}, 학점 : {sj['grd']}"
            break
    print(info)

# 성적 수정 시 이름을 통해 성적을 변수에 저장
def read_again(data, name):
    """
    성적 데이터 수정 시 수정할 데이터 입력받는 함수
    :param data: 기존에 저장된 성적 데이터
    :param name: 수정할 데이터의 이름
    :return: 수정된 성적데이터
    """
    kor = int(input(f"새로운 국어는? ({data['kor']})"))
    eng = int(input(f"새로운 영어는? ({data['eng']})"))
    mat = int(input(f"새로운 수학은? ({data['mat']})"))

    data = OrderedDict()
    data['name'] = name
    data['kor'] = kor
    data['eng'] = eng
    data['mat'] = mat

    return data

# 성적 데이터 수정/삭제 시 변경사항을 파일에 반영
def flush_sungjuk():
    """
    성적 데이터 수정/삭제 시 변경사항을 파일에 반영
    :return:
    """
    with open('sungjuk.json', 'w', encoding='utf-8') as f:
        json.dump(sjs, f, ensure_ascii=False)

#  성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return: 없음
    """
    print('성적데이터 수정')
    name = input('수정할 학생 이름은?')
    # 수정할 학생 데이터 찾기
    data = None
    idx = None
    for i, sj in enumerate(items) :
        if sj['name'] == name:
            data = sj
            idx = i
            break

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

# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터 삭제
    :param 없음:
    :return: 없음
    """
    print('성적데이터 제거')
    name = input('삭제할 학생 이름은?')
    # 삭제할 데이터 찾기
    data = None
    for sj in items:
        if sj['name'] == name:
            data = sj
            break
    # 찾은 데이터를 마지막으로 묻고 지우기
    if data :
        confirm = input('정말로 삭제하시겠습니까? (yes, no) :')
        if confirm == 'yes':
            items.remove(data)
            print(f'{name}의 데이터가 삭제되었습니다')
            sjs['response']['body']['totalCount'] -= 1
            flush_sungjuk()
        else :
            print('삭제가 취소되었습니다')

# 프로그램 종료
def exit_program():
    """
    sungjuk program exit
    :return: None
    """
    print('프로그램을 종료합니다')
    sys.exit(0)