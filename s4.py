import requests
from lxml import etree
response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/pear/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
dhrefs = eroot.xpath("//pre/a[position()>1]/@href")
dnames = eroot.xpath("//pre/a[position()>1]/@href")
dlinks=[]
#hrefs.reverse()
#names.reverse()
for dhref in dhrefs:
    dhref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/pear/"+ dhref
    dlinks.append(dhref) 

xd = 0
yd = 0
for dname in dnames:
     print("Find out the Package: "+dname)
     if (xd == yd):
          dimage=requests.get(dlinks[xd])
          with open("/mnt/e/pear/" + dname,'wb') as f:
               f.write(dimage.content)
               print("Downloading  " + dname + "  Please wait patiently !")
               print("\n")
          yd = yd+1
     xd = xd+1
print("Successfully downloaded all of the "+ str(xd)+" Packages !")