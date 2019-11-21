import requests
from lxml import etree

response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/newifi/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
ghrefs = eroot.xpath("//pre/a[position()>1]/@href")
gnames = eroot.xpath("//pre/a[position()>1]/@href")
glinks=[]
#hrefs.reverse()
#names.reverse()
for ghref in ghrefs:
    ghref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/newifi/"+ ghref
    glinks.append(ghref) 

xg = 0
yg = 0
for gname in gnames:
     print("Find out the Package: "+gname)
     if (xg == yg):
          gimage=requests.get(glinks[xg])
          with open("/mnt/e/newifi/" + gname,'wb') as f:
               f.write(gimage.content)
               print("Downloading  " + gname + "  Please wait patiently !")
               print("\n")
          yg = yg+1
     xg = xg+1
print("Successfully downloaded all of the "+ str(xg)+" Packages !")