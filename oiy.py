#download packages belong to kmods
import requests
from lxml import etree
"""response = requests.get(
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
          with open("///mnt//f//kmod//" + aname,'wb') as f:
               f.write(aimage.content)
               print("Downloading  " + aname + "  Please wait patiently !")
               print("\n")
          ya = ya+1
     xa = xa+1
print("Successfully downloaded all of the "+ str(xa)+" Packages !")

 


#download the base ipk
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
          with open("///mnt//f//base//" + bname,'wb') as f:
               f.write(bimage.content)
               print("Downloading  " + bname + "  Please wait patiently !")
               print("\n")
          yb = yb+1
     xb = xb+1
print("Successfully downloaded all of the "+ str(xb)+" Packages !")
"""




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
          with open("///mnt//f//lafit//" + cname,'wb') as f:
               f.write(cimage.content)
               print("Downloading  " + cname + "  Please wait patiently !")
               print("\n")
          cy = cy+1
     cx = cx+1
print("Successfully downloaded all of the "+ str(cx)+" Packages !")




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
          with open("///mnt//f//pear//" + dname,'wb') as f:
               f.write(dimage.content)
               print("Downloading  " + dname + "  Please wait patiently !")
               print("\n")
          yd = yd+1
     xd = xd+1
print("Successfully downloaded all of the "+ str(xd)+" Packages !")




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
          with open("///mnt//f//luci//" + ename,'wb') as f:
               f.write(eimage.content)
               print("Downloading  " + ename + "  Please wait patiently !")
               print("\n")
          ey = ey+1
     ex =ex+1
print("Successfully downloaded all of the "+ str(ex)+" Packages !")




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
          with open("///mnt//f//packages//" + fname,'wb') as f:
               f.write(fimage.content)
               print("Downloading  " + fname + "  Please wait patiently !")
               print("\n")
          fy = fy+1
     fx = fx+1
print("Successfully downloaded all of the "+ str(fx)+" Packages !")




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
          with open("///mnt//f//newifi//" + gname,'wb') as f:
               f.write(gimage.content)
               print("Downloading  " + gname + "  Please wait patiently !")
               print("\n")
          yg = yg+1
     xg = xg+1
print("Successfully downloaded all of the "+ str(xg)+" Packages !")




""" response = requests.get(
    url="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/pear/",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
             }
)
html = response.text

eroot = etree.HTML(html)
hhrefs = eroot.xpath("//pre/a[position()>1]/@href")
hnames = eroot.xpath("//pre/a[position()>1]/@href")
hlinks=[]
#hrefs.reverse()
#names.reverse()
for hhref in hhrefs:
    hhref="https://downloads.pangubox.com/pandorabox/19.01/packages/mipsel_24kec_dsp/pear/"+ hhref
    hlinks.append(hhref) 

hx = 0
hy = 0
for hname in hnames:
     print("Find out the Package: "+hname)
     if (hx == hy):
          himage=requests.get(hlinks[hx])
          with open("///mnt//f//pear//" + hname,'wb') as f:
               f.write(himage.content)
               print("Downloading  " + hname + "  Please wait patiently !")
               print("\n")
          hy = hy+1
     hx = hx+1
print("Successfully downloaded all of the "+ str(hx)+" Packages !")


 """
