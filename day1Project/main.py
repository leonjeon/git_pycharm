# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 파이썬에서 함수 만들기 : def 키워드 사용함
# def 함수명(매개변수): 
# 들여쓰기 함수의 실행 코드 작성함
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test_function():
    a = 1         # 정수형
    b = '1'       # 문자형
    c = 1.1      #실수형
    d = True    #논리형
    e = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999 #정수형
    f = 4 + 1j   #복소수 ('complex')
    # 파이썬에서는 바이트 사이즈로 정해지지 않는다. 정수면 정수, 실수면 실수
    print(type(a), type(b), type(c), type(d), type(e), type(f))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 함수 실행 :   함수명(전달인자) 또는 변수 = 함수명(전달인자)
    print_hi('PyCharm') # 함수 실행 구문
    a = '안녕'
    b = '하세요'
    print(a + b)
    test_function() # 함수 실행
    print('main 종료')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
