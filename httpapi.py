import httplib
import urllib2
from urllib2 import Request, urlopen, URLError

def http_connects(site,page):
 #checks if page is up  if its up it returns its text message/contents
    connect = httplib.HTTPConnection(site)
    connect.request("GET",page)
    request1 = connect.getresponse()
    print request1.status, request1.reason
        
    try:
            link="http://"+site+page
            requesturl = urllib2.Request(link, headers={'User-Agent' : "Mozilla"})
            opencon = urllib2.urlopen(requesturl)
            print opencon.read()        
    except URLError, e:
        print 'wrong entry', e
    connect.close()
    
http_connects("www.technologynet.co.ke", "/andela.html")
