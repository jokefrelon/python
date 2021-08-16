#coding=utf-8
import requests
from lxml import etree
import datetime

webPage = requests.get(url = "https://cn.bing.com/?FORM=BEHPTB&ensearch=1",
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
        )
we = webPage.text
ssr = etree.HTML(we)

# 已弃用 Links = ssr.xpath("//div/div[@id='bgDiv']/div/@data-ultra-definition-src")
staticLink = ssr.xpath("//div[@class='img_cont']/@style")
link=staticLink[0].split("(")[1].split(")")[0].split("&")[0].replace("1920x1080","UHD")
realink="https://cn.bing.com"+link
# 已弃用 Desc=ssr.xpath("//a/div/h2/text()")
Description=ssr.xpath("//h1[@class='text']/text()")
desc=Description[0]


print("")
print(datetime.datetime.now())
print(desc)

print("")
print(datetime.datetime.now())
print(realink)

picfile="/home/frelon/Bing_pic/pic/"+desc+".jpg"
picture=requests.get(realink)
with open (picfile,"wb+") as f:
         f.write(picture.content)
