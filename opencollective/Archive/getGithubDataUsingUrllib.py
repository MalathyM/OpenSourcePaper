import socket
import csv
import urllib.request
import json

if(socket.gethostname()=='c063144'):
    path='C:\\Users\\vivek4\\Downloads\\gitterFiles\\'
else:
    path='F:\\'


f = open(path+'Twitter+GitHub.csv', 'r', encoding="utf8")

urllist = []
readfile = csv.reader(f)
for row in readfile:
   urllist.append(row[5])
f.close()
#print(urllist)

newurllist = []
xlist = ['https://github.com', 'http://github.com']
for each in urllist:
   for x in xlist:
       if x in each:
           newurllist.append(each.replace(x,"https://api.github.com/repos"))
#print(newurllist)


myUrl = newurllist[2]
#head = {'Content-Type': 'application/json','Authorization': 'token {}'.format(myToken)}
response = urllib.request.urlopen(myUrl).read()

data_m=json.loads(response.decode('utf-8'))

response=urllib.request.urlopen('https://api.github.com/repos/nestjs/nest/contributors').read()
data_m=json.loads(response.decode('utf-8'))



