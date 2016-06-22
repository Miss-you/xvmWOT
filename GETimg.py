#_*_ coding: utf-8_*_

import urllib
import urllib2
import re
import os
import shutil
  
def getImg(html):
    #http://ww2.sinaimg.cn/large/d030806ajw1f53845zoo3j20my0g1di1.jpg 
    reg = r'http://ww[0-9].sinaimg.cn/.+?\.jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist 

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

#保存文件
def saveFile(target, data):
    if data == None:
        return
    
    file=open(target, "wb")
    file.write(data)
    file.flush()
    file.close()

#根据照片连接下载照片
def downImg(html_imgList, imgSerial):
    picPath = '/Users/yousa/Desktop/pic/' + str(imgSerial)
    
    if len(html_imgList) == 0:
        print ("html_imgList is None")
        return
    
    #清理过去图片
    if os.path.exists(picPath):
        shutil.rmtree(picPath)
        
    os.makedirs(picPath)  
     
    imgNo = 1
    
    for imgurl in html_imgList:
        #print imgurl
        filename = str(imgNo) + '.jpg'
        imgNo = imgNo + 1
        target = picPath + '/' + filename
        saveFile(target, getHtml(imgurl, None, headers))
          
    
#url = 'http://www.jdlingyu.com/'
#11992
url = 'http://www.jdlingyu.com/'
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25'
headers = { 'User-Agent' : user_agent }

def downloadHtmlImg(imgSerial):
    imgUrl = url + str(imgSerial)
    print imgUrl
    
    #get page
    page = getHtml(imgUrl, None, headers)
    if page == None:
        print(imgUrl + "unavailable!")
        return
        
    #get img list
    imglist = getImg(page)
    imglist = list(set(imglist))
    #download img
    downImg(imglist, imgSerial)
    
#for i = 0; i < 5; i++:
def run():
    for i in range(0, 25):
        #print i
        downloadHtmlImg(11992 - i)

run()

'''
page = getHtml(url, None, headers)

imglist = getImg(page)
print imglist

downImg(imglist)
'''