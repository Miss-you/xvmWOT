import re
import urllib

'''
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
'''

#http://blog.csdn.net/qq_15437667

import urllib2
 
req = urllib2.Request('http://blog.csdn.net/qq_15437667')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.code   
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
else:
    print "OK"