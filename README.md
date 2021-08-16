# 爬虫合集

## s series

s系列是我写的一个可以爬取pandoraboxd固件所对应软件包的爬虫,语法简单,主要调用了requests和lxml这两个模块,
反正在用之前需要安装这两货。我是用的python3写的爬虫脚本,python2 环境没有试过

```
pip install requests
pip install lxml
```

无聊写了一个爬虫,用来爬取某网站的Beauty 图片,可是代码写完了,发现已经被网站拉黑了
spi.py我也不能执行了,就放到git上充数

## Bing 每日图片爬虫

最近微软更新了 [bing.com](https://bing.com)的页面，之前的爬虫已经不能正常的爬取图片了，所以现在更新了一下
图片来源使用的国际版，并非国内版。本人博客也已更新 [JokemeBlog](https://jokeme.top)。

## spi.py && spider.py

这些都是以前无聊写的爬取小姐姐照片的，现在因该是不能用了，也不想更新代码了就这样吧。

## get.py && getM3u8.py

get.py是在学校的时候，搞大数据时需要采集数据写的爬虫，模拟采集某招聘网站的用户信息，爬取到的部分数据在wuli.json
getM3u8.py 是获取某网站上的m3u8视频链接。该网站目前已无法访问。
