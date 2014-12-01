#!/opt/local/bin/python
import urllib2

req = urllib2.Request('http://www.python.org')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
