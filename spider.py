import requests
from lxml import etree

webPage = requests.get(
	url="http://so.redocn.com/sucai/646f67.htm",
	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
	)
html = webPage.text
eroot = etree.HTML(html)
pic_url = eroot.xpath("//div/dl/dd/a/img/@src")
pic_name = eroot.xpath("//div/dl/dd/a/img/@alt")
urList=[]
nameList=[]
for pic in pic_url:
	print (pic)
	urList.append(pic)
a = 0
for name in pic_name:
	
	# print("hello name")
	if(a < len(urList)):
		pic_download = requests.get(url=urList[a],headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"})
		print("hello world"+str(a))
		with open ("D:/pic/"+name+".jpg",'wb') as picDown:
			picDown.write(pic_download.content)
			print("下载完成")
	a=a+1