# 2.2.1 urlparse : https://docs.python.org/3.5/library/urllib.parse.html
"""
scheme : URL에 사용된 프로토콜
netloc : 네트워크 위치. [user:password@host:port]로 표현하며, HTTP 경우 host:port
path : 파일이나 애플리케이션 경로
params : 애플리케이션에 전달될 매개변수
query : 질의 문자열로, &로 구분된 key:value로 표시
fragment : 문서 내의 앵커 등 조각을 지정
"""
from urllib.parse import urlparse, ParseResult


result_parse = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
assert isinstance(result_parse, ParseResult)
print(result_parse)
print(result_parse.scheme)
print(result_parse.netloc)
print(result_parse.path)
print(result_parse.params)
print(result_parse.query)
print(result_parse.fragment)


