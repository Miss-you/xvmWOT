import urllib
import urllib2
import re
  
#Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13
#Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25 

#61.172.249.96:80

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist 
    
def getArticleHtml(html):
    reg = r'[3-9][0-9]{7}'
    htmlre = re.compile(reg)
    arthtmllist = re.findall(htmlre,html)
    return arthtmllist     

def getHtml(url, values, headers):
    data = urllib.urlencode(values)  
    request = urllib2.Request(url, data, headers) 
#    request = urllib2.Request('http://www.xxxxx.com')

    try:
		response = urllib2.urlopen(request, timeout=10)
    except urllib2.HTTPError, e:
        print e.code   
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason     
    else:
        page = response.read()
    
    return page   

url = 'http://www.qiushibaike.com/'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'  
values = {'username' : 'ww770666',  'password' : '5591632w'}
headers = { 'User-Agent' : user_agent , 			'Referer': 'http://blog.csdn.net/'} 
#enable proxy
'''
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://218.75.100.114:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)
'''

#use safari Agent
page = getHtml(url, values, headers)

#print page
#print getImg(page)
#htmllist = getArticleHtml(page)
#print htmllist


