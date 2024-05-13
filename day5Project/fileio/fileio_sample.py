# path : fileio\\fileio_sample.py
# module : fileio.fileio_sample

# 파이썬에서의 파일입출력 처리
# open() --> writer() or read() --> closer()
'''
파일변수 = open('디렉토리명\\파일명.확장자', '열기모드')
파일입출력의 기본은 텍스트(문자)파일 입출력임
열기모드 :
w(wt), x(xt) : 새로 쓰기

 - w(wt) : 대상 파일이 없으면 파일을 자동으로 새로 만들어서 열기함
                대상 파일이 있으면, 파일 안의 내용을 모두 지우고 새로 쓰기 상태로 열기함

 - x(xt) :  대상 파일이 없을 때, 파일을 자동으로 새로 만들어서 열기함(기본적으로 새로쓰기)
                대상 파일이 있으면 에러 발생함 (wt 와 차이점)

 - r(rt) : 읽기 전용

 - a(at) : append - 추가 쓰기
                대상 파일이 없으면 파일을 자동으로 새로 만들어서 열기함
                대상 파일이 있으면, 파일 안의 내용을 그대로 두고 열기함
'''

# 파일 새로 만들고 값 기록 저장하기
import os

def test_fwrite():
    f = open('testa.txt', 'w', encoding='UTF-8')  # 기본 경로는 프로젝트 폴더 아래에 저장된다.
    f.write('test file write running.')
    f.write('12345')
    f.write('파일에 저장 확인')    # 텍스트 파일 인코딩이 'ms949'  문자 셋임
    f.write('☆★☆★☆★☆★☆★☆★☆★')   # 한글과 기호문자는 꺠짐
    # 파일 open 시 인코딩 문자셋 지정하면 해결됨
    f.close()

    # os 모듈을 활욜하면 현재 작업중인 디렉토리 경로를 확인할 수 있음
    print(os.getcwd())

# 원하는 디렉토리(폴더)에 파일을 만들려면
# open() 함수 첫번째 인자에 전체경로명과 파일명을 함께 입력하면 된다.
# 경로(path)는 백슬러시(\) 이스케이프 문자를 반드시 2개로 표기해야 한다.
def test_fwrite2():
    # x 모드 : 대상 파일이 존재하면 FileExistsError 발생함 ( 덮어쓰기 방지용 주로 사용함 )
    f = open('C:\\python_workspace\\day5Project\\fileio\\testb.txt', 'x', encoding='UTF-8')
    f.write('show me the money\n')
    f.write('99999999\n')
    f.write('경로를 포함해서 파일 지정 확인\n')
    f.write('2024년 04월 25일 아빠 생일이당\n')
    f.close()

# a 모드 : append (추가쓰기 모드)
# 기존 내용 다음에 추가됨
def test_fwrite3():
    f = open('testc.txt', 'a', encoding='UTF-8')
    f.write('test file append running\n')
    f.write('파일의 기존 내용 뒤에 추가쓰기 확인!!\n')
    f.close()   # append는 기존 내용애 계속 추가됨

# 파이썬에서 파일이나 디렉토리 다루기
# os 모듈이 제공하는 함수 사용함
def test_osmodule():
    # 사용 중인 컴퓨터의 사용자계정 (컴퓨터이름) 조회
    print(os.getlogin())
    # 현재 작업 디렉토리 조회
    print(os.getcwd())


    system_user = os.getlogin()
    # 디렉토리 만들기 : os.mkdir('만들 디렉토리 경로와 디렉토리명')
    work_dir = 'C:\\Users\\' + system_user + '\\Desktop\\python'
    # os.mkdir(work_dir)  # 주의 : 같은 이름의 디렉토리가 있으면 에러남
    os.chdir(work_dir)  # 현재 작업디렉토리 변경하기 : os.chdir('변경할 디렉토리명')
    print(os.getcwd())

    # 변경할 디렉토리에 파일 저장
    f = open('sample.txt', 'w', encoding='UTF-8')
    f.write('파이썬으로 디렉토리 만들고, 만든 디렉토리로 작업 폴더를 변경하였다.\n')
    st = '''변경된 디렉토리에 파일을 새로 만들고
    유니코드로 인코딩된 글자들을 기록 저장 확인함'''
    f.write(st)
    f.close()

# 리스트, 튜플, 셋, 딕셔너리 등에 저장한 데이터들을 파일에 저장
# writelines() 함수 사용
def test_writelines():
    tp = ('a', 'b', 'c')
    ls = ['r', 'e', 'd']
    f = open('list.txt', 'w')
    f.writelines(tp)
    f.write('\n')
    f.writelines(ls)
    f.write('\n')

    # 각 아이템별로 한 줄씩 기록을 원하면, write() 반복 실행하면 됨
    # f.write(ls)     # write() 는 str 만 사용할 수 있음, 리스트 사용 못 함
    for data in ls:
        f.write(str(data))  # 문자가 아닌 아이템은 str() 사용한다.
        f.write('\n')

    f.close()

# r(rt, read text) 읽기 전용
# 주의 : 대상 파일 없으면 에러남
# read() : 파일 전체 내용을 한 번에 읽음
# readline() : 파일 안의 내용을 한 줄씩 읽음
#                  마지막 라인을 읽고나서, 더 이상 읽을 라인이 없으면 None 리턴함 (자바에서는 -1 리턴함)
# readlines() : 파일의 내용을 줄 단위(아이템)로 모두 읽어서 리스트로 반환함
def test_fread():
    print(os.getcwd())
    # f = open('sample.txt', 'r', encoding='UTF-8')
    f = open('testb.txt', 'r', encoding='UTF-8')
    # print(f.read())

    # 파일의 내용을 한 줄씩 읽도록 처리한다면
    while True:
        line = f.readline()
        if not line:    # line  변수의 값이 없다면, None 이면...
            break
        print(line, end='')

    f.close()

def test_fread2():
    f = open('testb.txt', 'r', encoding='UTF-8')
    flist = f.readlines()
    print(flist)
    f.close()











if __name__ == '__main__':
    # test_fwrite()
    # test_fwrite2()
    # test_fwrite3()
    # test_osmodule()
    # test_writelines()
    # test_fread()
    test_fread2()








