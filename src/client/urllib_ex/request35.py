# Request 예제
from urllib.parse import quote
from urllib.request import Request, urlopen

from config import CLIENT_ID, CLIENT_SECRET
from src.client.urllib_ex.urlopen35 import EXAMPLE_URL


def print_request():
    req = Request(EXAMPLE_URL)
    req.add_header("Content-Type", "text/plain")
    req.add_header("query", "python")
    print(urlopen(req).read().decode('utf-8'))


# API 인자들(Python 기본 예제)
encText = quote("신촌로 150")
url = "https://openapi.naver.com/v1/map/geocode?query=" + encText
request = Request(url)
request.add_header("X-Naver-Client-Id", CLIENT_ID)
request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)


# Naver 지도 API에서 채움 주소 일부로 GPS 좌표 검색(GET method)
def print_naver_urlopen():
    response = urlopen(request)
    print(response.read().decode('utf-8'))


# main(start point)를 지정해줘야함
if __name__ == '__main__':
    print_request()
    print("\n")
    print_request()
