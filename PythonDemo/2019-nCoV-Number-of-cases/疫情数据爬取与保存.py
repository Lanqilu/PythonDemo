# -*- coding: utf-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup

dates = {
    "0326": "2020032710300",
    "0325": "2020032610291",
    "0324": "2020032510276",
    "0323": "2020032410263",
    "0322": "2020032310250",
    "0321": "2020032210237",
    "0320": "2020032110225",
    "0319": "2020032010210",
    "0318": "2020031910191",
    "0317": "2020031810176",
    "0316": "2020031710138",
    "0315": "2020031610125",
    "0314": "2020031510112",
    "0313": "2020031410103",
    "0312": "2020031310088",
    "0311": "2020031210075",
    "0310": "2020031110061",
    "0309": "2020031010046",
    "0308": "2020030910033",
    "0307": "2020030810016",
    "0306": "2020030710001",
    "0305": "2020030609985",
    "0304": "2020030509963",
    "0303": "2020030409947",
    "0302": "2020030309923",
    "0301": "2020030209901",
    "0229": "2020030109892",
    "0228": "2020022909862",
    "0227": "2020022809843",
    "0226": "2020022709829",
    "0225": "2020022609812",
    "0224": "2020022509791",
    "0223": "2020022409774",
    "0222": "2020022309758",
    "0221": "2020022209739",
}

for date in dates.items():
    url = "http://wjw.wuhan.gov.cn/front/web/showDetail/" + str(date[1])

    ls = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0'}]

    res = requests.get(url=url, headers=dict(random.choice(ls)))

    if res.status_code == 200:
        res.encoding = "utf-8"
        res = res.text
        html = BeautifulSoup(res, "html.parser")
        try:
            data = html.findAll("", {"class": "TRS_Editor"})
        except:
            break
    else:
        print("获取失败")


    def text_save(filename, data):
        file = open("./Data/" + filename, 'w', encoding="utf-8")
        s = str(data)
        s = re.sub("<.+?>", "", s)
        print("{}:{}".format(date[0], s))
        file.write(s)
        file.close()


    text_save("{}.txt".format(date[0]), data)

print("程序结束")
