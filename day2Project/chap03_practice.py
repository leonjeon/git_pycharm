# chap03_practice.py
# 문자자료형 실습문제

'''
 키보드로 입력받아 요구대로 처리하고 출력하시오.
 입력 내용 :
  회원이름 : 이순신 (member_name : str)
  회원아이디 : leess88@ict.org (member_id : str)
  패스워드 : pass1234 (member_passwd : str)
  나이 : 45 (age : int)
  키 : 187.5 (height : float)
출력 내용 : format() 메소드 사용함
 이순신 회원의 아이디는 leess88@ict.org 이고, 암호는 pass**** 입니다.
 나이는 45세이고, 키는 187.5 cm 입니다.
 - 출력시 처리조건 :
    암호는 첫글자부터 4글자만 슬라이싱한 다음 나머지 글자수에 맞춰서     * 로 출력되게 함
    키는 소숫점아래 첫자리까지만 출력되게 포멧팅함
'''

member_name = input('회원이름 : ')
member_id = input('회원아이디 : ')
member_passwd = input('패스워드 : ')
age = int(input('나이 : '))
height = float(input('키 : '))

# 패스워드의 일단 문자 길이를 알아내고, 알아낸 길이를 알아낼 변수하나 만든다.
# 만든 변수의 기존 변수 위 문제처럼 4번째 글자까지 자르고, 나머지 뒤부터 * 모양으로 출력되게끔  변수하나 더 생성 마지막엔 출력엔 이 변수를 쓴다
pass_pwd = len(member_passwd)
hidden_pwd = member_passwd[0:4] + ((pass_pwd - 4) * '*')

print(f'{member_name}회원의 아이디는 {member_id} 이고, 암호는 {hidden_pwd} 입니다. 나이는 {age}세이고, 키는 {height:.1f} cm 입니다.')


