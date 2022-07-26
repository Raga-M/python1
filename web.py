import re, urllib
import urllib.request
webpage=urllib.request.urlopen("https://www.flipkart.com/")
data=webpage.read()
#print(data)
phonenumber=re.findall("[0-9-]{7}[0-9-]+",str(data),re.I)
for number in phonenumber:
    print(number)