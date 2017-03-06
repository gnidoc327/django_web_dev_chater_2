# https://docs.python.org/3.5/library/http.server.html
from http.server import HTTPServer, CGIHTTPRequestHandler


if __name__ == '__main__':
    address = ("", 8888)

    httpd = HTTPServer(address, CGIHTTPRequestHandler)
    httpd.serve_forever()


