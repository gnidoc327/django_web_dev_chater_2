# -*- coding: utf-8 -*-
# http.server : https://docs.python.org/3.5/library/http.server.html
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(b'Hello World')    # input data is bytes


if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler)
    print('Started WebServer on port 8080...')
    print('Press ^C to quit WebServer')

    server.serve_forever()
