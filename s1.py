import requests
from lxml import etree
response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/targets/ralink/mt7620/packages/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
ahrefs = eroot.xpath("//pre/a[position()>1]/@href")
anames = eroot.xpath("//pre/a[position()>1]/@href")
alinks=[]
#hrefs.reverse()
#names.reverse()
for ahref in ahrefs:
    ahref="https://downloads.pangubox.com/pandorabox/19.01/targets/ralink/mt7620/packages/"+ ahref
    alinks.append(ahref) 

xa = 0
ya = 0
for aname in anames:
     print("Find out the Package: "+aname)
     if (xa == ya):
          aimage=requests.get(alinks[xa])
          with open("/mnt/e/kmod/" + aname,'wb') as f:
               f.write(aimage.content)
               print("Downloading  " + aname + "  Please wait patiently !")
               print("\n")
          ya = ya+1
     xa = xa+1
print("Successfully downloaded all of the "+ str(xa)+" Packages !")
