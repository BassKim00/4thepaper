from django import setup
import os, sys, re
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    proj_path = "/Users/leeuram/2018Project/botwarehouse"
    sys.path.append(proj_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mirae.settings")
    setup()

from stock.models import *


class InfoData:

    def __init__(self):
        pass

    def getInfoData(self):
        rows = Stock.objects.filter(id=1)

        for row in rows:
            if row.code is None:
                if "보통주" in row.name:
                    real_name = row.name.replace("보통주", "")
                else:
                    real_name = row.name
                url = self.makeUrlString(real_name)
                source_code = requests.get(url)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, 'lxml')
                tags = soup.findAll("td", class_="tit")

                if(len(tags) > 0):
                    m = re.compile(r'\d\d\d\d\d\d')
                    code_match = m.search(str(tags[0]))
                    row.code = code_match.group()
                    row.save()
                    print(code_match.group())
            else:
                print(row.name)

    def makeUrlString(self, real_name):
        url = 'https://finance.naver.com/search/searchList.nhn?query='
        url = url + real_name
        url = str(url.encode("euc-kr")).split('\'')[1]
        url = url.replace("\\x", "%")
        return url


if __name__ == '__main__':
    e = InfoData()
    e.getInfoData()
