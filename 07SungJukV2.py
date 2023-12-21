# 성적 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 입력데이터 선언
names = ['Seungjae', 'Suji', 'Samsung']
kors = [92, 60, 78]
engs = [88, 46, 89]
mats = [56, 99, 78]

#성적처리
tots = [kors[0] + engs[0] + mats[0], kors[1] + engs[1] + mats[1], kors[2] + engs[2] + mats[2]]
avgs =[tots[0] / 3, tots[1] / 3, tots[2] / 3]

print(f'{name:s}님의 성적은 국어는 {kor}점, 영어는 {eng}점, 수학은 {mat}점으로, '
      f'총점은 {tot:d}점이며, 평균은 {avg:.1f}점입니다.')
print('{}님의 성적은 국어는 {}점, 영어는 {}점, 수학은 {}점으로, '
      '총점은 {}점이며, 평균은 {}점입니다.'.format(
name, kor, eng, mat, tot, int(avg)
))
for i in range(0,3):
      print('%s님의 성적은 국어는 %d점, 영어는 %d점, 수학은 %d점으로, '
            '총점은 %d점이며, 평균은 %d점입니다.'
            % (names[i], kors[i], engs[i], mats[i], tots[i], int(avgs[i])
      ))