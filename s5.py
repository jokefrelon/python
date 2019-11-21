import requests
from lxml import etree
response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/luci/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
ehrefs = eroot.xpath("//pre/a[position()>1]/@href")
enames = eroot.xpath("//pre/a[position()>1]/@href")
elinks=[]
#hrefs.reverse()
#names.reverse()
for ehref in ehrefs:
    ehref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/luci/"+ ehref
    elinks.append(ehref) 

ex = 0
ey = 0
for ename in enames:
     print("Find out the Package: "+ename)
     if (ex == ey):
          eimage=requests.get(elinks[ex])
          with open("/mnt/e/luci/" + ename,'wb') as f:
               f.write(eimage.content)
               print("Downloading  " + ename + "  Please wait patiently !")
               print("\n")
          ey = ey+1
     ex =ex+1
print("Successfully downloaded all of the "+ str(ex)+" Packages !")