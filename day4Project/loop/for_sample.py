# loop/for_sample.py
# loop.for_sample
# 파이썬에서의 for 문 사용 테스트 스크립트
'''
for 문 작성형식 1 :
for 변수 in 리스트 | 튜플 | 딕셔너리 | 집합 | 문자열:
    반복실행할 구문들 작성 (들여쓰기)
주의사항 : in 오른쪽에 값하나(리터럴) 사용 못 함
for 변수 in 값: => TypeError 발생함
'''

def test_for1():
    for i in [10, 20, 30]:  # list 사용
        print(f'{i}는 5의 배수이다')

        # for k in 10:
        #     print(k)
    for t in (11, 22, 33):    # tuple 사용
        print(f'{t} 는 짝수이다.' if t % 2 == 0 else f'{t} 는 홀수다.')

    for s in {1, 2, 3, 4, 5, 6}:    # set 사용
        print(f'{s} 의 제곱은 {s**2}이다')
        
    for st in 'Python': # str 사용
        print(f'{st}문자의 유니코드는 {ord(st)}이다')


'''
for 문 작성형식 2 : range
range(시작값, 끝값) 또는 range(시작값, 끝값, 간격) 또는 range(끝값)
시작값 >= 0 | n, m > 끝값 간격은 생략시 기본 1임, 반드시 정수만 사용함
for 변수 in range(start, end): (콜론 주의)
    변수를 사용한 반복실행 구문 작성 (들여쓰기)
'''

# 1부터 100까지 정수들의 합계를 구해서 출력
def for_sum():
    sum = 0
    for n in range(1, 101):
        print(n, '+', end='')
        sum += n
    print()
    print(f'합계 : {sum}')

# --------------------------------------------------------------------------------------------
# import collections.iterable => deprecated : 버전 업하면서 사용이 중지됨
import collections.abc

def test_iterable():
    nlist = [1, 2, 3, 4]
    # iterable object: 리스트처럼 순차적으로 값을 가진 객체를 말함
    # isinstance() 함수 : 객체의 종류를 확인할 때 사용함 (자바의 instanceOf 연산자와 같음)
    print(isinstance(nlist, collections.abc.Iterable))  # Iterable 의 첫글자는 대문자임

def test_range():
    print(range(10))    # range(0, 10)

    lst = list(range(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(lst)

# for 문 작성형식 3 : range(len(리스트변수)) - 연속된 값을 인덱스로 처리
def for_indexing():
    # 리스트에 저장된 아이템 추출
    list1 = ['apple', 90, [1, 2, 3], ('A', 'B', 'C')]
    for item in list1:
        print(item)

        # 리스트의 저장 아이템을 인덱스를 이용해서 처리한다면
        for idx in range(len(list1)):
            print(list1[idx])






























