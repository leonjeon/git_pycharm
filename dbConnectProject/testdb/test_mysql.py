# path : testdb\\test_mysql.py

# 파이썬 외부 모듈(패키지) 설치와 사용
# 파이썬 외부 모듈은 프로젝트에 직접 설치해서 사용하는 방법이 있고 ( venv )
# 아나콘다에 별도의 콘다환경을 준비해서 필요한 패키지를 따로 설치한 다음에 프로젝트에 가져다가 사용하는 방법 (conda)이 있다.

# 프로젝트에 직접 설치하는 방법
# 첫번쨰 :
# 파이참 툴 왼쪽 아래의 'Python Packages' 탭을 클릭 > 뷰가 아래쪽에 보여짐
# 뷰의 왼쪽에 검색 영역에 설치할 패키지명을 입력
# 검색되면 패키지명을 클릭하면, 오른쪽에 패키지 정보가 표시됨
# 오른쪽 패키지 정보 위에 'Install Package' 버튼 클릭함 > 설치가 완료되면, 버전 숫자 표시됨
# 만약, 설치가 실패하면 오류 메세지에서 에러 이유를 찾아내서 해결해야 됨

# 두번째 :
# 모든 파이썬 개발툴에서 공통으로 사용하는 방법
# 'Terminal' (터미널) 탭 (왼쪽 아래) 클릭
# (가상환경종류) 터미널종류 현재프로젝트 경로> 프롬포트 표시됨
# 프롬포트에 설치 명령어를 직접 입력해서 설치함
# > pip install 설치할 패키지명
# 주의사항 : pip 버전을 먼저 upgrade 해야 되는 경우가 있음
# > python -m pip install --upgrade pip
# > pip --version
# 패키지 설치와 pip 업그레이드 동시에 수행할 수도 있음
# > python -m pip install --upgrade 설치할 패키지명

# 데이터베이스 연결에 필요한 파이썬 패키지 --------------------------------------------------------------
# mysql db : pymysql 패키지 필요
# oracle db : cx-Oracle 패키지 필요