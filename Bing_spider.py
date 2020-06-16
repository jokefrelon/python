#coding=utf-8
import requests
from lxml import etree
import datetime

webPage = requests.get(url = "https://cn.bing.com/?FORM=BEHPTB&ensearch=1",
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
        )
we = webPage.text
ssr = etree.HTML(we)
Links = ssr.xpath("//div/div[@id='bgDiv']/div/@data-ultra-definition-src")
Desc=ssr.xpath("//a/div/h2/text()")

Str="https://cn.bing.com"
desc=""
re = []
for sein in Desc:
        desc=sein
print(datetime.datetime.now())
print(desc)

for  se  in Links:
        Str = Str+se
        re = Str.split("&",1)
        Str=re[0]
print(datetime.datetime.now())
print(Str)
picfile="pic/"+desc+".jpg"
picture=requests.get(Str)
with open (picfile,"wb+") as f:
        f.write(picture.content)
print(datetime.datetime.now())
print("Get The Picture of Bing Successfully! "+"The Picture in \""+picfile+"\"")
