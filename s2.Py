import requests
from lxml import etree
response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/base/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
bhrefs = eroot.xpath("//pre/a[position()>1]/@href")
bnames = eroot.xpath("//pre/a[position()>1]/@href")
blinks=[]
#hrefs.reverse()
#names.reverse()
for bhref in bhrefs:
    bhref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/base/"+ bhref
    blinks.append(bhref) 

xb = 0
yb = 0
for bname in bnames:
     print("Find out the Package: "+bname)
     if (xb == yb):
          bimage=requests.get(blinks[xb])
          with open("/mnt/e/base/" + bname,'wb') as f:
               f.write(bimage.content)
               print("Downloading  " + bname + "  Please wait patiently !")
               print("\n")
          yb = yb+1
     xb = xb+1
print("Successfully downloaded all of the "+ str(xb)+" Packages !")