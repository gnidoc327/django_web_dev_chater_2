# 2.2.2 urllib2 : https://docs.python.org/3.5/library/urllib.request.html#module-urllib.request
from urllib.request import urlopen


# 예제 URL
EXAMPLE_URL = "http://www.example.com"

# Naver API 가이드 : https://developers.naver.com/docs/map/overview/
NAVER_URL = "http://www.naver.com"


# Naver 메인 페이지 출력
def print_urlopen():
    result_urlopen = urlopen(NAVER_URL)
    print(result_urlopen.read().decode('utf-8'))    # read(300) == 300 bytes만 읽어오겠다


# post 예제. data는 string이 아닌 bytes로 변환 시켜서 사용
def post_ex():
    data = "query=python"
    response = urlopen(EXAMPLE_URL, data.encode())
    print(response.read().decode('utf-8'))


# main(start point)를 지정해줘야함
if __name__ == '__main__':
    print_urlopen()
    print("\n")
    post_ex()

