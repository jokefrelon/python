# 利用Python爬虫获取bing.com每天的高清壁纸

众所周知,必应是主力做壁纸の搜索引擎!

每天都更新搜索页面的背景图片,这些图片也的的确确很好看,那我们要是♥心动了,想保存欣赏欣赏怎么办呐?

## 方法一:直接开发者模式拿图片

这个方法应该是最简单的了,`ctrl+ shift+i` 

```html
... ...
<tbody>
  <tr>
    <td id="hp_cellCenter" ... ...>
      <div id="hp_container" ... ...>
        <div id="bgDiv" ... ...>
          <div id="bgImgProgLoad" data-ultra-definition-src="/th?id=OHR.WildflowersBC_EN-CN3359054435_UHD.jpg&amp;rf=LaDigue_UHD.jpg&amp;pid=hp&amp;w=1920&amp;h=1080&amp;rs=1&amp;c=4" data-explicit-bing-load="false" data-dynamic-size="true">
            </div>
... ...		
```

这个链接🔗就在 `<div id="bgImgProgLoad"` の标签里面,复制 `data-ultra-definition-src` 所对应的值,再在前面补上`cn.bing.com` 就可以啦

不过这种方法下载的图片是被压缩以后的图片,大小也就几百kb,而如果我们想要下载原图的话,就需要把链接🔗里面第一个`.jpg` 后面的字符全给干掉,最终的的 **URL** 应该是: `https://cn.bing.com/th?id=OHR.WildflowersBC_EN-CN3359054435_UHD.jpg`

## 方法二:python爬虫

没有什么好说の,都是最简单的python命令,

运行环境: `Linux`

Python版本: `Python3`

pip依赖库: `requests,lxml`

基本上大部分的 **Linux** 都会预装 **Python3** ,所以就从安装 **pip** 开始了

```shell
sudo apt install python3-pip
pip3 install lxml
pip3 install requests
mkdir -p ~/Bing_pic/pic/
cd Bing_pic
nano xxx.py					#名字就根据你自己的喜好来吧,把下面的代码粘进去就可以啦
python3 xxx.py				#如果没有报错,大功告成啦
ls pic/						#看一下下载的壁纸
```

```python
#coding=utf-8
import requests
from lxml import etree
import os
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
print(desc)

for  se  in Links:
        Str = Str+se
        re = Str.split("&",1)
        Str=re[0]
print(Str)
picfile="pic/"+desc+".jpg"
picture=requests.get(Str)
with open (picfile,"wb+") as f:
        f.write(picture.content)
print("Get The Picture of Bing Successfully! "+"The Picture in \""+picfile+"\"")
```

如果你想每天都自动执行这段代码的话,就可以用 `crontab` 来定时执行

```shell
crontab -e
30 0 * * * python3 ~/Bing_pic/Bing_spider.py >> ~/Bing_pic/Bing_spider_log.txt
```

这样的话,每天凌晨12:30就会自动执行该命令啦

使用须知:这个脚本爬取的是 **Bing** 国际版的图片,所以当天中午12:00以后爬取的图片和第二天中午12:00之前爬取的图片一致,也就是第一天会出现这种情况,以后都没有问题的