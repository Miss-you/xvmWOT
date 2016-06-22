#_*_ coding: utf-8_*_

import urllib
import urllib2
import re
import os
  
#Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13
#Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25 

#61.172.249.96:80



def getImg(html):
    #reg = r'"http://ww[0-9].sinaimg.cn/large/(.+?\.jpg)"'
    reg = r'http://ww[0-9].sinaimg.cn/large/.+?\.jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist 
#http://ww2.sinaimg.cn/large/d030806ajw1f53845zoo3j20my0g1di1.jpg
    
def getArticleHtml(html):
    reg = r'[3-9][0-9]{7}'
    htmlre = re.compile(reg)
    arthtmllist = re.findall(htmlre,html)
    return arthtmllist     

#获取网页信息
def getHtml(url, values, headers):
    if values != None :
        data = urllib.urlencode(values)  
        request = urllib2.Request(url, data, headers) 
    else :
        request = urllib2.Request(url, headers = headers) 

    try:
		response = urllib2.urlopen(request, timeout=10)
    except urllib2.HTTPError, e:
        print e.code   
        return None
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason   
        return None  
    else:
        page = response.read()
    
    return page   

def saveFile(target, data):
    if data == None:
        return
    
    file=open(target, "wb")
    file.write(data)
    file.flush()
    file.close()

def downImg(html_imgList):
    picPath = '/Users/yousa/Desktop/pic'
    imgNo = 1
    
    #if not os.path.exists(picPath):
    #    os.makedirs(picPath) 
        
    for imgurl in html_imgList:
        print imgurl
        filename = str(imgNo) + '.jpg'
        imgNo = imgNo + 1
        target = picPath + '/' + filename
        #urllib.urlretrieve(imgurl, target)
        saveFile(target, getHtml(imgurl, None, headers))
          
    
#url = 'http://www.jdlingyu.com/'
url = 'http://www.jdlingyu.com/11894/'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
headers = { 'User-Agent' : user_agent }
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  

#enable proxy


#use safari Agent
#page = getHtml(url, values, headers)



#save_file('/Users/yousa/Desktop/pic', '1.jpg', getHtml('http://ww4.sinaimg.cn/large/d030806ajw1f538470z1gj22bc3h0476.jpg', None, headers)) 

   

page = getHtml(url, None, headers)

imglist = getImg(page)
print imglist

downImg(imglist)


'''

# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
</\>    print content
##<div class="mlr mt10 content-text">([\u000d\u000a\u4e00-\u9fa5\uff00-\uff20\u3002]+)<\/div>
    pattern = re.compile('<div.*?class="mlr.*?mt10.*?content-text>.*?([\u000d\u000a\u4e00-\u9fa5\uff00-\uff20\u3000-\u3010]+).*?<\/div>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
  
'''