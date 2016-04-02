import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist      
   
html = getHtml("http://tieba.baidu.com/p/4453124021?fr=frs")
print html
print getImg(html)

http://imgsrc.baidu.com/forum/w%3D580/sign=309cb23e29dda3cc0be4b82831e83905/95a9fc88d43f8794df68638fd51b0ef419d53ae3.jpg