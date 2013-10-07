from socket import *
import re
s=socket(AF_INET,SOCK_STREAM)
host='localhost'
port=8010
s.bind((host,port))
s.listen(4)
while True:
	c,addr=s.accept()
	data=c.recv(1024)
	match=re.search(r'GET\s/([\w.]+)',data)
	c.send(open(match.group(1)).read())
	c.close()
