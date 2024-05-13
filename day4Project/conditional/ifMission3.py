# conditional\\ifelseMission3.py
# conditional.ifelseMission3
# if else 실습문제
'''
키보드로 값을 입력받아 조건에 따라 처리하고 결과 출력하시오.
입력 내용 :
  수험번호 : 220602033 (tno : str)
  데이터베이스 : 90 (database : int)
  프로그래밍언어 : 98 (program : int)
  소프트웨어공학 : 60 (software : int)
처리 내용 :
  3과목의 총점(tot : int)과 평균(avg : int)을 계산함
  조건 처리 : 3과목 모두 40점이상이고, 평균이 60점이상이면
            수험번호 : 220602033 합격입니다. 출력
        아니면,
            수험번호 : 220602033 불합격입니다. 출력
'''
def practice3():
    tno = input('수험번호 : ')
    database = int(input('데이터베이스 : '))
    program = int(input('프로그래밍언어 : '))
    software = int(input('소프트웨어공학 : '))
    tot = int(database + program + software)
    avg = int(tot / 3)
    if database >= 40 and program >= 40 and software >= 40 and tot >= 60:
        print(f'수험번호 : {tno} 합격입니다.')
    else:
        print(f'수험번호 : {tno} 불합격입니다.')