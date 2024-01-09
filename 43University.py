class Student:
    def __init__(self, hakbun, name, addr, birth, dept, prof):
        self.hakbun = hakbun
        self.name = name
        self.addr = addr
        self.birth = birth
        self.dept = dept
        self.prof = prof

    def __str__(self):
        info = f'{self.hakbun} {self.name} {self.addr} {self.birth} {self.dept} {self.prof}'
        return info


class Professor:
    def __init__(self, name, major, tech, subject):
        self.name = name
        self.major = major
        self.tech = tech
        self.subject = subject

    def __str__(self):
        info = f'{self.name} {self.major} {self.tech} {self.subject}'
        return info


class Subject:
    def __init__(self, number, name, summary, section, prof):
        self.number = number
        self.name = name
        self.summary = summary
        self.section = section
        self.prof = prof

    def __str__(self):
        info = f'{self.number} {self.name} {self.summary} {self.section} {self.prof}'
        return info


class Depart:
    def __init__(self, dname, dpos, phone, chair):
        self.dname = dname
        self.dpos = dpos
        self.phone = phone
        self.chair = chair

    def __str__(self):
        info = f'{self.dname} {self.dpos} {self.phone} {self.chair}'
        return info


class StudentMange():
    def __init__(self):
        self.students = {}

    def add_student(self, s):
        self.students[s.number] = 1

seungjae = Student(1, '승재', '서울시 관악구', '19980706', '전자공학과', '김철수')
seungjae.addr = '경기도 고양시'
kimho = Professor('김호', '전자공학', ['자바', '파이썬'], '컴퓨터 공학의 이해')
programming = Subject('0205', '프로그래밍', '자바 프로그래밍', '컴퓨터', 301)
computer = Depart('컴퓨터공학', 'E동 2층', '123-547-8912', 504)

print(seungjae)
print(kimho)
print(programming)
print(computer)

