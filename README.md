# 9xD Django 스터디
## Chapter 2 : Python 웹 표준 라이브러리
### Description
* ppt - slideshare :
* 개발환경
  * python 3.5 : [download link](https://www.python.org/downloads/release/python-350/)
  * pycharm : [download link](https://www.jetbrains.com/pycharm/download/#section=windowscommunity) - Windows, Mac, Linux 모두 지원(Windows 중점으로 진행)
    * Professional 권장(유료 or [대학교 Email 인증시 무료](https://www.jetbrains.com/shop/eform/students)), Community(무료) 
  * Windows 유저의 경우, etc/[get-pip.py](https://bootstrap.pypa.io/get-pip.py)를 실행하여 pip upgrade 할 것
  
### 목차
    2.1 웹 라이브러리 구성
    2.2 웹 클라이언트 라이브러리
        2.2.1 urlparse 모듈 
            - [참고자료](https://docs.python.org/3.5/library/urllib.parse.html)
        2.2.2 urllib2 모듈
        2.2.3 urllib2 모듈 예제
        2.2.4 httplib 모듈
        2.2.5 httplib 모듈 예제
    2.3 웹 서버 라이브러리
        2.3.1 간단한 웹 서버
        2.3.2 BaseHTTPServer 모듈
        2.3.3 SimpleHTTPServer 모듈
        2.3.4 CGIHTTPServer 모듈
        2.3.5 xxxHTTPServer 모듈 간의 관계
    2.4 CGI/WSGI 라이브러리
        2.4.1 CGI 관련 모듈
        2.4.2 WSGI 개요
        2.4.3 WSGI 서버의 애플리케이션 처리 과정
        2.4.4 wsgiref.simple_server 모듈
        2.4.5 WSGI 서버 동작 확인

### Directory 구조
    * root
        * etc
            * get-pip.py - windows pip upgrade(python get-pip.py로 실행)
            
        * src
            * application.py - 예제 연습
            
        * config.py - Naver API 등 설정값 
