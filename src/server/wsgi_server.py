# https://docs.python.org/3.5/library/wsgiref.html
from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults


def my_app(environ, start_response):
    setup_testing_defaults(environ)

    status = "200 OK"
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return ["This is a sample WSGI Application."]

if __name__ == '__main__':
    print("Started WSGI Server on port 8888...")
    server = make_server('', 8888, my_app)
    server.serve_forever()

