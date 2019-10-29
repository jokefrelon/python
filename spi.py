import requests
from lxml import etree
import os
import time
from fake_useragent import UserAgent
webpage = requests.get(url="http://m.win4000.com/meitu_4_1.html",
headers = {'User-Agent':UserAgent().random})

html_document = webpage.text
etree_H=etree.HTML(html_document)
webPage_URL = etree_H.xpath("//div[@class='img_cont']/ul/li/a/@href")
webPage_URL_Pic_name = etree_H.xpath("//div[@class='img_cont']/ul/li/a/img/@alt")

URL_PIC = []
FOLDER_NAME = []

for pic_url in webPage_URL:
    print(pic_url)
    URL_PIC.append(pic_url)

for name_url in webPage_URL_Pic_name:
    FOLDER_NAME.append(name_url)
    print(name_url)
           
unmberX = 0

for folder in FOLDER_NAME:
    path = "d:/jpg/"+str(folder)
    print (folder)
    os.mkdir(path)
    with open (path+"/"+str(FOLDER_NAME[0])+".txt",'a') as file:
        file.write(URL_PIC[unmberX])
    if (unmberX <= len(URL_PIC)):
        unmberX+=1
    time.sleep(0.4)
    for new_URL in URL_PIC:
        frelon = 1
        welcome = []
        welcome.append(new_URL)
        for se in welcome:
            second_webpage = requests.get(welcome[-1],headers={'UserAgent':UserAgent().random})
            second_html_document = second_webpage.text
            second_etree_HTML = etree.HTML(second_html_document)
            second_webPage_URL = second_etree_HTML.xpath('//div[@class="xq_cont"]/a/img/@src')
            NextPage_URL = second_etree_HTML.xpath('//div[@class="xq_cont"]/a/@href')
            etc = []
            alipay = []
            for picsss in second_webPage_URL:
                etc.append(picsss)
                sman = requests.get(etc[0],headers={'UserAgent':UserAgent().random})
                with open (path+"/"+frelon+".png",'wb') as florensa :
                    florensa.write(sman)
                frelon+=1
            for urlllll in NextPage_URL:
                alipay.append(urlllll)
                sman = requests.get(alipay[0],headers={'UserAgent':UserAgent().random})
                swoman = sman.text
                swoman_HTML = etree.HTML(swoman)
                # swoman_URL = swoman_HTML.xpath('//div[@class="xq_cont"]/a/img/@src')
                sNextwoman = swoman_HTML.xpath('//div[@class="xq_cont"]/a/@href')
                for ssl in sNextwoman:
                    welcome.append(ssl)
            

# webPage2 = requests.get(url=URL_PIC[unmberX],
# headers = {"User-Agent" : "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36"})
# WebPageHTML = webPage2.text
# etree_Second = etree.HTML(WebPageHTML)
# ThisPage_PIC_URL = etree_Second.xpath('//div[@class="xq_cont"]/a/img/@src')
# NextPage_URL = etree_Second.xpath('//div[@class="xq_cont"]/a/@href')




