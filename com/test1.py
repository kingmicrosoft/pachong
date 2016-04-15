
import urllib2
import urllib
from  urllib2 import Request, urlopen, URLError, HTTPError
import cookielib
import re

str1="America"
str2="china"
ab=0
url="http://www.baidu.com/"
result=eval('ab+100')
print(result)
exec('a=100')
# print(a)
str_="my,word,is,worth,your,trust"
list1=str_.split(",")
print list1[0],  list1[1] ,list1[2]
if str_.startswith("my"):
    print('haha')
else:
    print('not haha')
req=Request(url)
try:
    response = urllib2.urlopen(req)
    print "real url is:"+response.geturl()
except HTTPError,e:
    print 'Error code',e.code
except URLError,e:
    print 'Reson',e.reason
else:
    print "other code"
html = response.read()
#print html
# print response.

#cookie
cookie = cookielib.CookieJar()
opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
res =opener.open(url)
for item in cookie:
    print 'nama  '+item.name
    print 'value '+item.value


#reprocee

p = re.compile('?a.*script.*')
mat=p.match(html)
if mat==None :
    print mat
else :
    print mat.lastindex

