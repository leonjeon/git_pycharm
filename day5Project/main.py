# random test
# 랜덤 : 임의의 숫자(랜던값) 를 발생시키고자 할 때, random 모듈이 제공하는 함수를 사용할 수 있음
import random

def test_random():
    print('임의의 랜덤값 : ', random.random())
    # 0.0 <= 랜덤값 < 1.0 범위의 실수형 값 발생

    print('랜던값 확인 : ', random.randrange(1, 11))
    # start <= 랜덤값 < stop 범위의 정수형 값 발생함

# 1부터 45까지의 임의의 정수 6개를 중복되지 않게 발생시켜서 저장하고
# 오름차순으로 정렬해서 출력 처리
def lotto():
    # print('1 ~ 45 의 정수 발생: ', random.randrange(1, 45))
    # random.randrange(1, 45)

    #
    num = set()
    while len(num) < 6:
        num.add(random.randrange(1,45))
    # 함수 이용 sort, sorted 둘 중 하나선택
    num1 = list(num)
    # sort 함수를 사용해서 오름차순 정렬
    # reverse : 리스트의 저장 순서를 반대로 뒤집기하는 함수
    num1.sort(reverse=False)
    print(num1)
    print(sorted((num1)))








# 함수 실행
if __name__ == '__main__':
    # test_random()
    lotto()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
