import urllib2

response=urllib2.urlopen('http://182.18.61.50/search.html')
urlmsg=response.read()
print urlmsg
#response=urllib2.urlopen('http://blog.csdn.net/qq_15437667/article/details/50957996')
