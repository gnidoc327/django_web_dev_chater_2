from urllib.request import ProxyHandler, ProxyBasicAuthHandler, build_opener

# 설명을 위한 코드라고 함
proxy_handler = ProxyHandler()
proxy_auth_handler = ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = build_opener(proxy_handler, proxy_auth_handler)
response = opener.open("http://www.example.com/login.html")


