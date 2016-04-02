#import urllib2
#import urllib


#response=urllib2.urlopen('http://182.18.61.50/search.html')
#urlmsg=response.read()
#print urlmsg
#response=urllib2.urlopen('http://blog.csdn.net/qq_15437667/article/details/50957996')


#values = {"username":"794089112@qq.com","password":"lhy19970512"}
#data = urllib.urlencode(values) 
#url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#request = urllib2.Request(url,data)
#response = urllib2.urlopen(request)
#print response.read()

#url = 'http://www.douban.com'
#info = {'name' : 'Michael Foord',
#          'location' : 'Northampton'}
#data = urllib.urlencode(info)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#the_page = response.read()
#print the_page


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