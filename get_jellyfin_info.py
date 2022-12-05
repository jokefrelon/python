import requests
from lxml import etree
import os

def getweb(link,xpa):
	response = requests.get(
    	url=link,
    	headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    )

	html = response.text
	eroot = etree.HTML(html)
	return eroot.xpath(xpa)

def getffmpeglink(jellyfinFFmpegBaseLink,jellyfin_ffmpeg):
	sys_version = None
	jellyfin_ffmpeg_deb = None
	with open('/etc/os-release','r') as f:
		for er in f:
			if er.find('VERSION_ID') != -1:
				sys_version = er.split('"')[1]
	if sys_version == "18.04":
		jellyfin_ffmpeg_deb = jellyfinFFmpegBaseLink + jellyfin_ffmpeg[0] + "jellyfin-ffmpeg5_"+ jellyfin_ffmpeg[0].replace("/","") + "-bionic_amd64.deb" 
	
	elif sys_version == "20.04":
		jellyfin_ffmpeg_deb = jellyfinFFmpegBaseLink + jellyfin_ffmpeg[0] + "jellyfin-ffmpeg5_"+ jellyfin_ffmpeg[0].replace("/","") + "-focal_amd64.deb"
	
	elif sys_version == "22.04":
		jellyfin_ffmpeg_deb = jellyfinFFmpegBaseLink + jellyfin_ffmpeg[0] + "jellyfin-ffmpeg5_"+ jellyfin_ffmpeg[0].replace("/","") + "-jammy_amd64.deb"
	return jellyfin_ffmpeg_deb


jellyfinFFmpegBaseLink = "https://repo.jellyfin.org/releases/server/ubuntu/versions/jellyfin-ffmpeg/"
jellyfin_ffmpeg=getweb(jellyfinFFmpegBaseLink,"//pre/a[last()]/@href")
jellyffpeglink = getffmpeglink(jellyfinFFmpegBaseLink,jellyfin_ffmpeg)
fflink = "wget " + jellyffpeglink
os.system(fflink)

jellyfinMetaBaseLink = "https://repo.jellyfin.org/releases/server/ubuntu/versions/stable/meta/"
jellyfin_meta = getweb(jellyfinMetaBaseLink,"//pre/a[last()]/@href")
jellyfinmetalink = jellyfinMetaBaseLink+jellyfin_meta[0]+"jellyfin_"+jellyfin_meta[0].replace("/","")+"-1_all.deb"
mtlink = "wget " + jellyfinmetalink
os.system(mtlink)

jellyfinServerBaseLink = "https://repo.jellyfin.org/releases/server/ubuntu/versions/stable/server/"
jellyfin_server = getweb(jellyfinServerBaseLink,"//pre/a[last()]/@href")
jellyfinserverlink = jellyfinServerBaseLink+jellyfin_server[0]+"jellyfin-server_"+ jellyfin_server[0].replace("/","") +"-1_amd64.deb"
svlink = "wget " + jellyfinserverlink
os.system(svlink)

jellyfinWebBaseLink = "https://repo.jellyfin.org/releases/server/ubuntu/versions/stable/web/"
jellyfin_web = getweb(jellyfinWebBaseLink,"//pre/a[last()]/@href")
jellyfinweblink = jellyfinWebBaseLink+jellyfin_web[0]+"jellyfin-web_"+ jellyfin_web[0].replace("/","") +"-1_all.deb"
wblink = "wget " + jellyfinweblink
os.system(wblink)