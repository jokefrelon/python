# Python爬虫🕷

用**python**写爬虫其实是比较简单的,主要还是靠第三方的库🆒常用的有 **requests & urllib** 至于解析HTML,我目前使用的是 **xpath** ,了解了基本操作,咱就试试看吧

### 代码附上

~~~python
# coding:utf-8
import json
import requests
from lxml import etree

def getWebUrl(uri):
	webPage = requests.get(url = uri,
		headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
		)

	we = webPage.text
	ssr = etree.HTML(we)
	
	Links = ssr.xpath("//div/table/tbody/tr/td/p/a/@href")

	Str = "http://172.17.150.251"
	Allinks = []

	for  se  in Links:
		link = Str+se
		Allinks.append(link)
	
	dicName = {}
	dicName = {uri:Allinks}
	return dicName

def getInfo(uri):
	webPage = requests.get(url = uri,
		headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
		)
	page = webPage.text
	pageinfo = etree.HTML(page)

	info = pageinfo.xpath("//div/span[@class='sp4']/text()")
	notNesInfo = pageinfo.xpath("//div/span[@class='sp2']/text()")
	salaryInfo = pageinfo.xpath("//div[@class='cn']/strong/text()")
	job = pageinfo.xpath("//p[position()=1]/span[@class='el']/text()")
	city = pageinfo.xpath("//span[@class='lname']/text()")

	if (len(notNesInfo)!=0):
		for er in notNesInfo:
			info.append(er)

	information = {"info":info,'salaryInfo':salaryInfo,'job':job,'city':city}

	return information


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
we = {}
fun = {}
tot = []
wilu = []
for a in range(1,41):
	strin = "http://172.17.150.251/xueqing-web/course/index/{}".format(a)
	tot.append(strin)
	we = getWebUrl(strin)
	fun.update(we)
	we.clear()
for osx in tot:
	wilu  = fun.get(osx)
	for xs in wilu:
		ufo = {}
		ufo = getInfo(xs)
		fuc ={xs:ufo}
		we.update(fuc)

wei = json.dumps(we,indent=1,ensure_ascii=False)
with open("wuli.json",'w',encoding='utf-8') as f:
	f.write(wei)
print("😘")
~~~

因为我是真的又菜又爱玩,所以才写的这么烂的代码😜,以后还是要慢慢提升啊

我爬取的是51job网站,可是如果爬虫大规模爬取,网站就会封IP,所以我就把页面抓下来,放到本地,开一个web服务器,慢慢调试代码代码🤷‍♂️

最基本的两个库,**requests & lxml**  **simplejson** 不是必要的,我只是为了把爬取到的数据保存到本地查看才出此下策,实在是菜的无奈😁才这样干了,其实我也是懒得配置数据库了

### 代码解释

**getWebUrl()** 是拿取网站一共有多少页并且获取该页面下的求职信息详情页面链接,再传递给下一个函数处理我给写死了

**getInfo()** 处理**geWebUrl()** 传递过来的详情页面链接,并爬取数据返回我需要的求职信息

还有需要注意的是json格式化**dict**Chinese时,非常容易乱码,所以在dumps()方法里,我没有用ascii,这也算是一个小坑吧,一开始的时候
我保存数据,不管用啥方法都乱码,心态都炸了,**# coding:utf-8**也用了,就是不奏效



### 爬取到的信息节选

~~~json
{
 "http://172.17.150.251/xueqing-web/51job/72396849.html": {
        "info": [
            "3-4年经验",
            "本科",
            "招1人",
            "02-08发布",
            "英语良好",
            "计算机科学与技术 自动化"
        ],
        "salaryInfo": [
            "15-28万/年"
        ],
        "job": [
            "软件工程师",
            "算法工程师"
        ],
        "city": [
            "广州"
        ]
    },
    "http://172.17.150.251/xueqing-web/51job/98287424.html": {
        "info": [
            "5-7年经验",
            "大专",
            "招若干人",
            "02-08发布"
        ],
        "salaryInfo": [
            "1-2万/月"
        ],
        "job": [
            "销售经理"
        ],
        "city": [
            "北京"
        ]
    },
    "http://172.17.150.251/xueqing-web/51job/98370374.html": {
        "info": [
            "5-7年经验",
            "本科",
            "招2人",
            "02-08发布"
        ],
        "salaryInfo": [],
        "job": [
            "高级软件工程师",
            "网站运营经理/主管"
        ],
        "city": [
            "深圳"
        ]
    },
    "http://172.17.150.251/xueqing-web/51job/97846012.html": {
        "info": [
            "无工作经验",
            "本科",
            "招若干人",
            "02-08发布",
            "英语熟练",
            "计算机科学与技术 计算机网络"
        ],
        "salaryInfo": [
            "10-15万/年"
        ],
        "job": [
            "系统工程师",
            "系统架构设计师"
        ],
        "city": [
            "北京-昌平区"
        ]
    },
    "http://172.17.150.251/xueqing-web/51job/96612644.html": {
        "info": [
            "无工作经验",
            "招若干人",
            "02-08发布"
        ],
        "salaryInfo": [
            "1-2万/月"
        ],
        "job": [
            "信息技术经理/主管"
        ],
        "city": [
            "北京-西城区"
        ]
    }
}
~~~

