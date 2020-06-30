# Python 爬虫抓取播放源(m3u8)

今天没有事的时候在捯饬 [dotPlayer](https://apps.apple.com/cn/app/id1455092592) [IOS平台APP/￥收费💴] 时发现这个东西是个宝贝呀!可以看 m3u8格式的视频,这都不是重点,重点是使用起来非常舒服,虽然直接复制m3u8链接到Safari也可以播放,但是 **dotPlayer** 还可以有封面和标题!这两者体验可谓是天差地别(我没有收钱哈!我是真的觉得好用,希望dotplayer的作者看到了打一下广告费!)

具体可以看

简书作者: [NickXXXXXXXX](https://www.jianshu.com/u/cac586f07bd4) 给出的图片简介

Github上的 [help_zh.md](https://github.com/frozenthrone/dotplayer/blob/master/help_zh.md) 给出的使用简介

这都不是我们需要关注の重点,重点是**这款app是用来播放m3u8流の**

播放视频很简单,可是这 **m3u8** 文件从哪里来呢???

1. 去 `Telegram` 加入组群  [dotPlayer](https://t.me/dotplayer) ,群里经常会分享相关的订阅
2. 自己动手丰衣足食

这次用的爬虫和上一次一模一样,只是我优化了一下过程,就随便讲讲吧

```python
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
```

整体分为三个部分:

```python
def makeUrl(Num):
def getRealUrl(fakeUrl):
def ownSource(realUrl):
```

### 1. def makeUrl(Num):

该函数,接收一个 `int` 类型的参数, **return** 一个`字符串列表`

这部分就是分析页面链接🔗的规则,在本地生成 **URL** ,并返回给下一个函数处理, 爬虫能在本地干的就经量在本地完成,不过度占用服务器的资源,不给站长添堵! 这也是为了自己好😂😂😂 俗话说的好:爬虫学的好! ... ...

### 2. def getRealUrl(fakeUrl):

该函数,接收一个 `字符串列表` **return** 一个 `嵌套列表`

这部分就是接收到上面生成の **URL** ,访问并分析网页结构.拿到视频的 **封面** **真实播放页** の URL,并且返回给下一个函数来执行

### 3. def ownSource(realUrl):

该函数,接收一个`嵌套列表` **return** 一个  `嵌套列表`

这部分也很简单,接收上面来的链接,一个一个的访问,拿到 **标题** **播放URL** ,然后返回一个 `嵌套列表` 

### 4. 编写代码

函数已经写好了,我们自己调用即可,需要注意循环嵌套的时候不能犯迷糊就可以,最后处理一下所得到の数据,写入本地json文件就可以了

虽然我爬虫很菜,但是我在一点点的学习!一起加油吧!!!

最新代码在 [Github](https://github.com/jokefrelon/python/blob/master/getM3u8.py) 上,这篇文章,以后就不更新了