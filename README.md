# 9xD Django 스터디
## Chapter 2 : Python 웹 표준 라이브러리
### Description
* ppt - slideshare : [ppt link](http://www.slideshare.net/HanSungKim4/django-study)
* 개발환경
  * python 3.5 : [download link](https://www.python.org/downloads/release/python-350/)
  * pycharm : [download link](https://www.jetbrains.com/pycharm/download/#section=windowscommunity) - Windows, Mac, Linux 모두 지원(Windows 중점으로 진행)
    * Professional 권장(유료 or [대학교 Email 인증시 무료](https://www.jetbrains.com/shop/eform/students)), Community(무료) 
  * Windows 유저의 경우, etc/[get-pip.py](https://bootstrap.pypa.io/get-pip.py)를 실행하여 pip upgrade 할 것
  
### 목차
    2.1 웹 라이브러리 구성
    2.2 웹 클라이언트 라이브러리
        2.2.1 urlparse 모듈 - urllib.urlparse
            - [참고자료](https://docs.python.org/3.5/library/urllib.parse.html)
        2.2.2 urllib2 모듈 - urllib.urlopen [GET], [POST]
            - [참고자료](https://docs.python.org/3.5/library/urllib.request.html#module-urllib.request)
        2.2.3 urllib2 모듈 예제 - image parser (urlopen 응용)
        2.2.4 httplib 모듈 - httplib [GET], [HEAD], [POST], [PUT]
            - [참고자료](https://docs.python.org/3.5/library/http.client.html)
        2.2.5 httplib 모듈 예제 - image download (image parser, httplib 응용)
    2.3 웹 서버 라이브러리
        2.3.1 간단한 웹 서버
        2.3.2 BaseHTTPServer 모듈 - http.server
            - [참고자료](https://docs.python.org/3.5/library/http.server.html)
        2.3.3 SimpleHTTPServer 모듈 - http.server
            - [참고자료](https://docs.python.org/3.5/library/http.server.html)
        2.3.4 CGIHTTPServer 모듈 - http.server --cgi (옵션 차이)
            - [참고자료](https://docs.python.org/3.5/library/http.server.html)
        2.3.5 xxxHTTPServer 모듈 간의 관계
    2.4 CGI/WSGI 라이브러리
        2.4.1 CGI 관련 모듈
        2.4.2 WSGI 개요
        2.4.3 WSGI 서버의 애플리케이션 처리 과정
        2.4.4 wsgiref.simple_server 모듈 - wsgiref.simple_server
            - [참고자료](https://docs.python.org/3.5/library/wsgiref.html)
        2.4.5 WSGI 서버 동작 확인 - 확인 못함(python3에서 2.4.4 코드 동작 안함)

### Directory 구조
    * [root]
        * application.py - 예제 연습(굳이 안써도 됩니다)
        * config.py - Naver API Client Key Value
        
        * [etc]
            * get-pip.py - windows pip upgrade(python get-pip.py로 실행)
            
        * [src]
            * requirements.txt - pip install -r /path/to/requirements.txt(필요 라이브러리 자동 설치)
            
            * [client] - 2.2 예제
                * [cgi_http_server_client] - 2.3.4 서버 요청 클라이언트 예제
                * [httplib_ex] - 2.2.4 ~ 5
                * [urllib_ex] - 2.2.1 ~ 3
           
            * [server] - 2.3, 2.4 예제
                * [cgi-bin] - cgi_http_server.py에서 사용(cgi script)
                * cgi_http_server.py - 2.3.4   
                * hello_world.py - 2.3.2
                * simple_http_server.py - 2.3.3
                * wsgi_server.py - 2.4.4
                