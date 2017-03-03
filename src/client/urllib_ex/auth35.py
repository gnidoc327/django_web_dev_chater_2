import urllib.request


URL = "http://www.example.com/login.html"


# 설명을 위한 코드라고 함
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen(URL)
print(response)

