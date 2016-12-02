import httplib
from urllib2 import Request, urlopen, URLError
 
conn = httplib.HTTPConnection("www.technologynet.co.ke")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.status, r1.reason

data1 = r1.read()
conn.request("GET", "/security.html")
r2 = conn.getresponse()
print r2.status, r2.reason

data2 = r2.read()
#
request = Request('http://technologynet.co.ke/index.html')

try:
	response = urlopen(request)
	rsp = response.read()
	print rsp[559:1000]
except URLError, e:
    print 'an error occured:', e
conn.close()
