# 성적 프로그램 v2
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 입력데이터 선언
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []

#성적 데이터 입력
for i in range(3):
      print(f'{i+1}번째 학생데이터 입력')
      names.append(input('이름은 ?'))
      kors.append(int(input('국어는 ?')))
      engs.append(int(input('영어는 ?')))
      mats.append(int(input('수학은 ?')))

#성적처리
for i in range(len(names)):
      tots.append(kors[i] + engs[i] + mats[i])
      avgs.append(tots[i] / 3)

#성적 출력
for i in range(len(names)):
      print(f'이름 : {names[i]:s}, 국어 : {kors[i]:d}, 영어 : {engs[i]:d}, '
            f'수학 : {mats[i]:.1f}, 합계 : {tots[i]:d}, 평균 : {avgs[i]:.2f}')

a = '334'
a.replace('!', '')
print(a)

for i in range(0,3):
      print('%s님의 성적은 국어는 %d점, 영어는 %d점, 수학은 %d점으로, '
            '총점은 %d점이며, 평균은 %d점입니다.'
            % (names[i], kors[i], engs[i], mats[i], tots[i], int(avgs[i])
      ))

n = input()
m = input()
#부등호를 인식하고, 인식된 부등호대로 값을 판단하고, 0과 1을 출력
int(2>=3)
('!', '>') == ('!', '>')