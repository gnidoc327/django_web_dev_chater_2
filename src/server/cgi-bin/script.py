import cgi

print("Content-Type: text/plain")
print("\r")
print("Wellcome, CGI Scripts")

form = cgi.FieldStorage()

for item in form.list:
    print(item.name)
    print(item.value)