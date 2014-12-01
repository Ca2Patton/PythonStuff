#!/opt/local/bin/python
import urllib
import urllib2

data = {}
data['name'] = "Caitlin Patton"
data['location'] = "California"
data['language'] = "Python"
url_values = urllib.urlencode(data)
print url_values

url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib2.urlopen(full_url)
