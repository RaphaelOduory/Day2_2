from urllib2 import urlopen

myapi = urlopen('https://graph.facebook.com/search?q=apigee&type=post')

f = open('facebook')
f.write(myapi.read())
f.close()