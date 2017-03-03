import os
from http import client
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve

from src.client.urllib_ex.parse_image import ImageParser

FOLDER_NAME = "DOWNLOAD_TEMP"


def download_image(src_url, data):
    if not os.path.exists(FOLDER_NAME):
        os.makedirs(FOLDER_NAME)

    parser = ImageParser()
    parser.feed(data)
    result_set = set(x for x in parser.result)

    for x in sorted(result_set):
        src = urljoin(src_url, x)
        basename = os.path.basename(src)
        target_file = os.path.join(FOLDER_NAME, basename)

        print("Downloading....", src)
        urlretrieve(src, target_file)


def main():
    host = "www.google.co.kr"

    conn = client.HTTPConnection(host)
    conn.request("GET", "")
    response = conn.getresponse()
    types = response.msg["Content-Type"].split(";")
    for _type in types:
        if "charset" in _type:
            charset = _type.split("=")[1]
            data = response.read().decode(charset)
            conn.close()

            print("\nDownload Images from", host)
            url = urlunparse(('http', host, '', '', '', ''))
            download_image(url, data)
            print("Fetch Images from", url)


if __name__ == '__main__':
    main()