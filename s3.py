import requests
from lxml import etree
response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/lafite/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
chrefs = eroot.xpath("//pre/a[position()>1]/@href")
cnames = eroot.xpath("//pre/a[position()>1]/@href")
clinks=[]
#hrefs.reverse()
#names.reverse()
for chref in chrefs:
    chref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/lafite/"+ chref
    clinks.append(chref) 

cx = 0
cy = 0
for cname in cnames:
     print("Find out the Package: "+cname)
     if (cx == cy):
          cimage=requests.get(clinks[cx])
          with open("/mnt/e/lafit/" + cname,'wb') as f:
               f.write(cimage.content)
               print("Downloading  " + cname + "  Please wait patiently !")
               print("\n")
          cy = cy+1
     cx = cx+1
print("Successfully downloaded all of the "+ str(cx)+" Packages !")