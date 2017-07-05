#coding=utf8

import httplib, urllib, Image, webbrowser, re

id = raw_input('id:')
httpClient = None
#get downcode
try:
    headers = {'Host':'dufile.com'
        ,'Connection':'keep-alive'
        ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3104.0 Safari/537.36'
        ,'Accept':'image/webp,image/apng,image/*,*/*;q=0.8'
        ,'Referer':'http://dufile.com/down/' +id+ '.html'
        ,'Accept-Encoding':'gzip, deflate'
        ,'Accept-Language':'zh-CN,zh;q=0.8'
        ,'Cookie':'PHPSESSID=0os2g6op33u4p954ufnmip5jm0'}    
    httpClient = httplib.HTTPConnection('dufile.com', 80, timeout=30)
    httpClient.request('GET', '/downcode.php', None, headers)

    response = httpClient.getresponse()
    with open('tmp.png', 'wb') as file:
        file.write(response.read())
    image = 'tmp.png'
    img = Image.open(image)
    img.show()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

downcode = raw_input('downcode:')
#img.close()

#post downcode
try:
    params = urllib.urlencode({'action':'yz', 'id':id, 'code':downcode})
    headers = {'Host':'dufile.com'
       ,'Connection':'keep-alive'
       ,'Accept':'text/plain, */*; q=0.01'
       ,'Origin':'http://dufile.com'
       ,'X-Requested-With':'XMLHttpRequest'
       ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3104.0 Safari/537.36'
       ,'Content-Type':'application/x-www-form-urlencoded'
       ,'Referer':'http://dufile.com/down/'+ id +'.html'
       ,'Accept-Encoding':'gzip, deflate'
       ,'Accept-Language':'zh-CN,zh;q=0.8'
       ,'Cookie':'PHPSESSID=0os2g6op33u4p954ufnmip5jm0'}
    
    httpClient = httplib.HTTPConnection('dufile.com', 80, timeout=30)
    httpClient.request('POST', '/downcode.php', params, headers)
    response = httpClient.getresponse()
    '''print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息'''
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

#get key
try:
    headers = {'Host':'dufile.com'
        ,'Connection':'keep-alive'
        ,'Upgrade-Insecure-Requests':'1'
        ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3104.0 Safari/537.36'
        ,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        ,'Referer':'http://dufile.com/down/' +id+ '.html'
        ,'Accept-Encoding':'gzip, deflate'
        ,'Accept-Language':'zh-CN,zh;q=0.8'
        ,'Cookie':'PHPSESSID=0os2g6op33u4p954ufnmip5jm0'}
    httpClient = httplib.HTTPConnection('dufile.com', 80, timeout=30)
    httpClient.request('GET', '/dd.php?file_key='+ id +'&p=1', None, headers)

    response = httpClient.getresponse()
    '''print response.status
    print response.reason
    print response.read()
    print response.getheaders() #获取头信息'''
    html = response.read()
    m = re.search(r'[a-zA-z]+://[^\s]*%[\w]*', html)
    url = m.group()
    print url
    webbrowser.open(url, new = 0, autoraise= True)
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()


#downurl

#webbrowser.open('dufile.com/dd.php?file_key='+ id +'&p=1', new = 0, autoraise= True)