# 성적 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

# 입력데이터 선언
name = 'Seungjae'
kor = 92
eng = 88
mat = 56

#성적처리
tot = kor + eng + mat
avg = tot / 3

print(f'{name:s}님의 성적은 국어는 {kor}점, 영어는 {eng}점, 수학은 {mat}점으로, '
      f'총점은 {tot:d}점이며, 평균은 {avg:.1f}점입니다.')
print('{}님의 성적은 국어는 {}점, 영어는 {}점, 수학은 {}점으로, '
      '총점은 {}점이며, 평균은 {}점입니다.'.format(
name, kor, eng, mat, tot, int(avg)
))
print('%s님의 성적은 국어는 %d점, 영어는 %d점, 수학은 %d점으로, '
      '총점은 %d점이며, 평균은 %d점입니다.' % (
name, kor, eng, mat, tot, int(avg)
))