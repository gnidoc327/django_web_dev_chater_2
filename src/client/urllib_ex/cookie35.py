from urllib.request import HTTPCookieProcessor, build_opener, install_opener, urlopen

# 설명을 위한 코드라고 함
cookie_handler = HTTPCookieProcessor()
opener = build_opener(cookie_handler)
install_opener(opener)
response = urlopen("http://www.example.com/login.html")

