from http import client
from urllib.parse import urlencode


def get():
    print("get method")
    conn = client.HTTPConnection("www.example.com")
    conn.request("GET", "/index.html")
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()
    conn.request("GET", "/parrot.spam")
    r2 = conn.getresponse()
    print(r2.status, r2.reason)

    data2 = r2.read()
    conn.close()


def head():
    print("\nhead method")
    conn = client.HTTPConnection("www.example.com")
    conn.request("HEAD", "/index.html")
    res = conn.getresponse()
    print(res.status, res.reason)

    data = res.read()
    print(len(data))

    print(data == b'')


def post():
    print("\npost method")
    params = urlencode({
        '@number': 12524,
        '@type': 'issue',
        '@action': 'show',
    })

    headers = {
        'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'
    }

    conn = client.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)

    print(response.read().decode("utf-8"))


# 예시코드
def put():
    pass


if __name__ == '__main__':
    get()
    head()
    post()

