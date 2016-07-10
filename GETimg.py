#_*_ coding: utf-8_*_

import urllib
import urllib2
import re
import os
import shutil
import sys



def getImgUrl(page):
    #http://ww2.sinaimg.cn/large/d030806ajw1f53845zoo3j20my0g1di1.jpg 
    reg = r'http://ww[0-9].sinaimg.cn/.+?\.jpg'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,page)
    return imglist 

def getImagepageHtml(page):
    reg = r'http://www.jdlingyu.com/[0-9]{5}/'
    imghtmlre = re.compile(reg)
    htmlList = re.findall(imghtmlre,page)
    return htmlList

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
#todo
def saveFile(target, data):
    if data == None:
        return
    
    file=open(target, "wb")
    file.write(data)
    file.flush()
    file.close()

#根据照片连接下载照片
def downImg(html_imgList, imgSerial):
    picPath = filePath + '/' + str(imgSerial)
    
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

def getImagepageHtmlSerial(imgPage):
    serial = filter(lambda x:x.isdigit(),imgPage)
    
    return serial

def downloadHtmlImg(pageNum):
    #get page
    if pageNum == 1:
        page = getHtml(url, None, headers)
    else:    
        html = url + 'page/' + str(pageNum)
        print html
        page = getHtml(html, None, headers)
    if page == None:
        print("main page unavailable!")
        return
        
    imghtmlList = getImagepageHtml(page)
    imghtmlList = list(set(imghtmlList))
    
    for imgHtml in imghtmlList:
        imgPage = getHtml(imgHtml, None, headers)
        if imgPage == None:
            print(imgHtml + "unavailable!")
            return
            
        #get img list
        imgList = getImgUrl(imgPage)
        imgList = list(set(imgList))
    
        imgSerial = getImagepageHtmlSerial(imgHtml)
        #download img
        downImg(imgList, imgSerial)
 
#获取脚本文件的当前路径
#def cur_file_dir():
def getCurFileDir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
     
    
#for i = 0; i < 5; i++:
def run():
    global filePath
    urllib2.socket.setdefaulttimeout(20) 
    filePath = getCurFileDir()
    print filePath
    for i in range(0, 1):
        #print i
        #downloadHtmlImg(1 + i)
        downloadHtmlImg(2 + i)


'''
#page = getHtml("http://www.jdlingyu.com/page/2/", None, headers)
page = getHtml("http://www.jdlingyu.com/", None, headers)
imghtmlList = getImagepageHtml(page)
imghtmlList = list(set(imghtmlList))
'''

#print getImgSerial("http://www.jdlingyu.com/11970/")

run()


