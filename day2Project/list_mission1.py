# list_mission1.py

"""
키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.

입력 내용 :
    학생이름 : 홍길동 (name : str)
    학년 : 2 (grade : int)
    반 : 3 (s_class : int)
    번호 : 12 (s_no : int)
    점수 : 87.5 (score : float)

처리 내용 :
    입력받은 값들을 리스트(student_list)에 순서대로 저장 처리함

출력 내용 :
    리스트에 저장된 값들을 출력함
    2학년 3반 12번 홍길동의 점수는 87.50 입니다.
    -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
"""
student_list = []

student_list.append(input('학생 이름 : '))
student_list.append(int(input('학년 : ')))
student_list.append(int(input('반 : ')))
student_list.append(int(input('번호 : ')))
student_list.append(float(input('점수 : ')))

print(f'{student_list[1]}학년 {student_list[2]}반 {student_list[3]}번 {student_list[0]}의 점수는 {student_list[4]} 입니다.')


"""    키보드로 값들을 입력받아, 요구대로 처리하고 확인 출력 코드를 작성하시오.
입력 내용 :
    국어 점수 : 78.5 (kor : float)
    영어 점수 : 88.7 (eng: float)
    수학 점수 : 93.5 (mat : float)
처리 내용 :
    3명의 학생 점수를 입력 받음, 각 학생의 총점과 평균은 각각 계산함
    학생별 점수는 각 리스트에 저장한 다음, [국어, 영어, 수학, 총점, 평균]
    각 학생 점수를 리스트(sungjuk_list)에 순서대로 저장 처리함
    [[국, 영, 수, 총, 평], [국, 영, 수, 총, 평], [국, 영, 수, 총, 평]]
    3명의 점수의 총합(total_score : int)과 전체평균(average_score : float)를
    계산하시오.
출력 내용 :
    리스트에 저장된 값들을 출력함,   국, 영, 수, 총, 평균 순서로 출력
     -> 점수는 소수점아래 둘째자리까지 표시
    -> format() 사용함
    전체 총점과 전체 평균을 출력하시오.
"""

sungjuk_list = []
total_score = 0
avrage_score = 0

kor1 = float(input('국어 점수 : '))
eng1 = float(input('영어 점수 : '))
mat1 = float(input('수학 점수 : '))
score1 = [kor1, eng1, mat1]
score1.append(kor1 + eng1 + mat1)
score1.append(score1[3] / 3)

kor2 = float(input('국어 점수 : '))
eng2 = float(input('영어 점수 : '))
mat2 = float(input('수학 점수 : '))
score2 = [kor2, eng2, mat2]
score2.append(kor2 + eng2 + mat2)
score2.append(score2[3] / 3)

kor3 = float(input('국어 점수 : '))
eng3 = float(input('영어 점수 : '))
mat3 = float(input('수학 점수 : '))
score3 = [kor3, eng3, mat3]
score3.append(kor3 + eng3 + mat3)
score3.append(score3[3] / 3)

sungjuk_list.append(score1)
sungjuk_list.append(score2)
sungjuk_list.append(score3)

# 첫번째 학생의 총점, 두번쨰 학생의 총점, 세번째 학생의 총점을 total_score에 넣어준다
total_score = sungjuk_list[0][3] + sungjuk_list[1][3] + sungjuk_list[2][3]

# 3명의 학생 총점을 9로 나누어 변수에 넣어준다
average_score = total_score / 9

# sungjuk_list 에 .append로 total_score 와 average_score를 넣어준다.
sungjuk_list.append(total_score)
sungjuk_list.append(average_score)

print(f''' 학생 1의 국어 점수 :{sungjuk_list[0][0]}, 영어 점수 : {sungjuk_list[0][1]}, 수학 점수 : {sungjuk_list[0][2]}, 총점 : {sungjuk_list[0][3]}, 평균 : {sungjuk_list[0][4]},
학생 2의 국어 점수 :{sungjuk_list[1][0]}, 영어 점수 : {sungjuk_list[1][1]}, 수학 점수 : {sungjuk_list[1][2]}, 총점 : {sungjuk_list[1][3]}, 평균 : {sungjuk_list[1][4]},
학생 3의 국어 점수 :{sungjuk_list[2][0]}, 영어 점수 : {sungjuk_list[2][1]}, 수학 점수 : {sungjuk_list[2][2]},총점 : {sungjuk_list[2][3]}, 평균 : {sungjuk_list[2][4]},
전체 총점 : {sungjuk_list[3]}, 전체 평균 : {sungjuk_list[4]}''')


