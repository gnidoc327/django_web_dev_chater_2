from html.parser import HTMLParser
from urllib.request import urlopen


class ImageParser(HTMLParser):
    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    data_set = set(x for x in parser.result)
    print('\n'.join(sorted(data_set)))


def main():
    url = "http://www.google.co.kr"
    f = urlopen(url)
    headers = f.info()
    types = headers["Content-Type"].split(";")
    for _type in types:
        if "charset" in _type:
            charset = _type.split("=")[1]
            data = f.read().decode(charset)
            f.close()

            print("Fetch Images from", url)
            parse_image(data)
            return

    print("charset not found", url)


if __name__ == '__main__':
    main()
