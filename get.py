# coding:utf-8
import json
import requests
from lxml import etree


def getWebUrl(uri):
    webPage = requests.get(url=uri,
                           headers={
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                           )

    we = webPage.text
    ssr = etree.HTML(we)

    Links = ssr.xpath("//div/table/tbody/tr/td/p/a/@href")

    Str = "http://172.17.150.251"
    Allinks = []

    for se in Links:
        link = Str+se
        Allinks.append(link)

    dicName = {}
    dicName = {uri: Allinks}
    return dicName


def getInfo(uri):
    webPage = requests.get(url=uri,
                           headers={
                               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
                           )
    page = webPage.text
    pageinfo = etree.HTML(page)

    info = pageinfo.xpath("//div/span[@class='sp4']/text()")
    notNesInfo = pageinfo.xpath("//div/span[@class='sp2']/text()")
    salaryInfo = pageinfo.xpath("//div[@class='cn']/strong/text()")
    job = pageinfo.xpath("//p[position()=1]/span[@class='el']/text()")
    city = pageinfo.xpath("//span[@class='lname']/text()")

    if (len(notNesInfo) != 0):
        for er in notNesInfo:
            info.append(er)

    information = {"info": info, 'salaryInfo': salaryInfo,
                   'job': job, 'city': city}

    return information


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
we = {}
fun = {}
tot = []
wilu = []
for a in range(1, 41):
    strin = "http://172.17.150.251/xueqing-web/course/index/{}".format(a)
    tot.append(strin)
    we = getWebUrl(strin)
    fun.update(we)
    we.clear()
for osx in tot:
    wilu = fun.get(osx)
    for xs in wilu:
        ufo = {}
        ufo = getInfo(xs)
        fuc = {xs: ufo}
        we.update(fuc)

wei = json.dumps(we, indent=1, ensure_ascii=False)
with open("wuli.json", 'w', encoding='utf-8') as f:
    f.write(wei)
print("😘")
