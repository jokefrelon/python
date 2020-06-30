#coding=utf-8
import requests
from lxml import etree
import time
import datetime
import re

def makeUrl(Num):
	# Num为html的页数
	allinks=[]
	for link in range(1,Num+1):
		link="https://weicha.cc/category/8/page/{}".format(link)
		allinks.append(link)
	return allinks

def getRealUrl(fakeUrl):
	webPage = requests.get(
		url=fakeUrl,
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
		)
	indexPage=webPage.text
	indexHtml=etree.HTML(indexPage)
	nextPageUrl=indexHtml.xpath("//div[@id='posts']/div[@class='post grid']/h3/a/@href")
	picurls=indexHtml.xpath("//div[@class='img']/a/img/@data-src")
	Set = []
	Set.append(nextPageUrl)
	Set.append(picurls)
	return Set

def ownSource(realUrl):
	webPagess = requests.get(
		url=realUrl,
		headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
	)
	indexPagess=webPagess.text
	indexHtmlss=etree.HTML(indexPagess)
	title=indexHtmlss.xpath("//header/h1/text()")
	source=indexHtmlss.xpath("//div[@class='article-content']/div/@data-item")
	finalUrl = []
	finalUrl.append(title)
	finalUrl.append(source)
	return finalUrl

Derailed = makeUrl(110)
# print(Derailed)
for iPhoneSE in Derailed:
	
	ceo = getRealUrl(iPhoneSE)
	qq = ceo[0]
	a=0
	for SourceUrl in qq:
		helloWorld = ownSource(SourceUrl)
		
		MUlink=helloWorld[1][0]
		realMULinks=MUlink.split('"')
		realMULink=realMULinks[5].replace("\\","")
		title=helloWorld[0][0].replace(" ","")
		thePicUrl = ceo[1][a]

		p=re.compile(r"[-,$()#+&*' ]")
		lastTitle=re.sub(p,"",title)
		
		str ='{\n'+'"name":"'+lastTitle+'",\n'+'"logo":"'+thePicUrl+'",\n'+'"url":"'+realMULink+'"\n'+'},\n'
		# print(str)
		with open ("weicha8.json","a+",encoding='utf-8') as f:
			f.write(str)
		a+=1
		print(str)
		print(a)
		print(datetime.datetime.now())
		time.sleep(1)