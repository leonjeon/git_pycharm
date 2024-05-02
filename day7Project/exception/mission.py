# path ; excetion\\mission.py
# 예외처리 실습문제

# 2단에서 9단까지의 구구단을 선택해서 한개의 단을 출력처리함
# 키보드로 출력할 단을 입력받아서 진행함
# 입력된 단수는 정수여야 함 (예외처리)
# 입력된 단수는  2~ 9 사이의 값이여야 구구단 출력됨
# 입력된 단수가 2보다 작으면 단수는 2로 처리함
# 입력된 단수가 9보다 크면 단수는 9로 처리함
# try: except: else: finally: 형식으로 작성함

def gugudan():
    try:
        dan = int(input('구구단 단수 : '))
    except ValueError:
        print('정수만 입력하시오.')
    else:
        if dan < 2:
            dan = 2
        elif dan > 9:
            dan = 9

        for su in range(int(1, 10)):
            print(f'{dan} * {su} = {dan * su}')
    finally:
        print('구구단 출력 종료입니다.')






if __name__ == '__main__':
    gugudan()