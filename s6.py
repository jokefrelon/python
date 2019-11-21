import requests
from lxml import etree
response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/packages/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
fhrefs = eroot.xpath("//pre/a[position()>1]/@href")
fnames = eroot.xpath("//pre/a[position()>1]/@href")
flinks=[]
#hrefs.reverse()
#names.reverse()
for fhref in fhrefs:
    fhref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/packages/"+ fhref
    flinks.append(fhref) 

fx = 0
fy = 0
for fname in fnames:
     print("Find out the Package: "+fname)
     if (fx == fy):
          fimage=requests.get(flinks[fx])
          with open("/mnt//e/packages/" + fname,'wb') as f:
               f.write(fimage.content)
               print("Downloading  " + fname + "  Please wait patiently !")
               print("\n")
          fy = fy+1
     fx = fx+1
print("Successfully downloaded all of the "+ str(fx)+" Packages !")