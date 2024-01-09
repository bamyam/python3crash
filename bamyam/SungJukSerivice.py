from bamyam.SungJuk import SungJuk

class SungJukSerivece:

    @staticmethod
    def read_sungjuk():
        name = input('이름은 ?')
        kor = int(input('국어는 ?'))
        eng = int(input('영어는 ?'))
        mat = int(input('수학은 ?'))

        return SungJuk(name, kor, eng, mat)

    @staticmethod
    def compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90): sj.grd = '수'
        elif (sj.avg >= 80): sj.grd = '우'
        elif (sj.avg >= 70): sj.grd = '미'
        elif (sj.avg >= 60): sj.grd = '양'

# 성적 서비스 호출1
sjsrv = SungJukSerivece() # Serivice 클래스에 대한 객체 생성
sj = sjsrv.read_sungjuk()
print(sj)

sjsrv.compute_sungjuk(sj)
print(sj)

# 성적 서비스 호출2
sj2 = SungJukSerivece.read_sungjuk() # 객체생성 없이 정적메서드로 실행
SungJukSerivece.compute_sungjuk(sj2)
print(sj2)

