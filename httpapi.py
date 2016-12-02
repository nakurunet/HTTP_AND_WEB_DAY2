import httplib
from urllib2 import Request, urlopen, URLError

def http_connects(site,page):
 #checks if page is up print 200 ok response
    connect = httplib.HTTPConnection(site)
    connect.request("GET",page)
    request1 = connect.getresponse()
    print request1.status, request1.reason

    data1 = request1.read()
    connect.request("GET", "/security.html")
    request2 = connect.getresponse()
    print request2.status, request2.reason 

    data2 = request2.read()
    #Gets facebook startpage html source
    request = Request('http://facebook.com/')

    try:
        response = urlopen(request)
        rsp = response.read()
        print rsp[559:1000]
    except URLError, e:
        print 'an error occured:', e
    connect.close()

http_connects("www.technologynet.co.ke", "/index.html")
