import pickle
import os

def emp_process():
    emp_dict = dict()

    prompt = '''
    *** 직원 정보 관리 프로그램 ***
    1. 새 직원정보 추가
    2. 직원정보 삭제
    3. 전체 출력
    4. 파일에 저장
    5. 파일로 부터 직원정보 읽어오기
    9. 프로그램 끝내기
    '''
    while True:
        print(prompt)
        no = int(input('번호 입력 : '))

        if (no == 1):
            empid = input('사번 : ')
            empname = input('이름 : ')
            empno = input('주민번호 : ')
            email = input('이메일 : ')
            phone = input('전화번호 : ')
            salary = int(input('급여 : '))
            job = input('직급 : ')
            dept = input('부서 : ')

            emp_dict[empid] = [empid, empname, empno, email, phone, salary, job, dept]
            print('새로운 직원 정보가 추가되었습니다.')

        elif (no == 2):
            print('현재 등록된 직원수는 %d 명입니다.' % len(emp_dict))
            key = input('삭제할 사번 : ')
            emp_dict.pop(key)
            print(key, '번 사번의 직원 정보가 삭제되었습니다.')

        elif (no == 3):
            for key, value in emp_dict.items():
                print('{} : {}'.format(key, value))

        elif (no == 4):
            fname = input('저장할 파일명 : ')
            f = open(fname, 'wb')
            pickle.dump(emp_dict, f)
            f.close()
            print('{} 파일에 성공적으로 저장되었습니다.'.format(fname))

        elif (no == 5):
            fname = input('읽을 파일명 : ')
            f = open(fname, 'rb')
            emp_dict = pickle.load(f)
            f.close()
            print(emp_dict)

        elif (no == 9):
            break

    print('직원 관리 프로그램이 종료되었습니다.')

# 프로그램 실행 ----------------------------------------------
if __name__ == '__main__':
    emp_process()