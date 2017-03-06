# https://docs.python.org/3.5/library/http.server.html
# 예제 실행 전 python -m http.server 8888 실행해보기(== SimpleHTTPServer[v2.7])
# python -m http.server --cgi 8888
from http import server
from http.server import HTTPServer


if __name__ == '__main__':
    handler = server.SimpleHTTPRequestHandler
    httpd = HTTPServer(("", 8888), handler)
    httpd.serve_forever()



