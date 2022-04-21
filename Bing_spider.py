#coding=utf-8
import requests
from lxml import etree
import datetime


def logout(desc,realink):
	print("")
	print(datetime.datetime.now())
	print(desc)

	print("")
	print(datetime.datetime.now())
	print(realink)

def saveimg(desc,realink):
	picfile="/home/frelon/Bing_pic/pic/"+desc+".jpg"
	picture=requests.get(realink)
	with open (picfile,"wb+") as f:
	         f.write(picture.content)

webPage = requests.get(
	url = "https://cn.bing.com/?FORM=BEHPTB&ensearch=1",
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
)
we = webPage.text
ssr = etree.HTML(we)

# image url
realink=ssr.xpath("//link[@id='preloadBg']/@href")[0].split("&")[0].replace("1920x1080","UHD").replace("s.cn.bing.net","www.bing.com")
print(realink)

# description 
desc=ssr.xpath("//meta[@property='og:title']/@content")[0]
print(desc)

# print log
logout(desc,realink)

# save image to file
saveimg(desc,realink)
