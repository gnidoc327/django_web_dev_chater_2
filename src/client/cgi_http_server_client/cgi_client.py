from urllib.request import urlopen

url = "http://localhost:8888/cgi-bin/script.py"

data = "language=python"

f = urlopen(url, data.encode())
print(f.read())

"""
r = requests.post(url, data={"language": "python"})
print(r.status_code)
print(r.text)
"""
