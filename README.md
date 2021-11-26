# NICO_CRAWL
니코동 크롤링 파이썬 코드


현재 올라온 코드 2개는 onetab을 이용한 링크 내보내기 기능을 이용하여야 작동이 가능합니다.

현재 파이썬 3.9버전/ 윈도우 환경에서만 정상적인 작동을 보증합니다.

selenium 라이브러리와 chromedriver.exe 설치가 필수입니다.

실행전 NICO_FILE_LOAD.py의 chromedriver.exe 경로지정을 하여야 합니다.


1.같은 파일에 NICO_FILE_LOAD.py와 NICO_AUTO_LOAD.py 파일을 같이 넣기.

2. NICO_FILE_LOAD.py 실행 후 Onetab을 이용하여 추출한 링크 붙여넣기
이 과정에서 '니코링크.txt'파일이 생성됩니다.

3. NICO_AUTO_LOAD.py 실행

4.결과적으로 '완료 리스트.txt" 파일이 생성됩니다.

