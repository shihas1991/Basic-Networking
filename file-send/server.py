from socket import *
import re
s=socket(AF_INET,SOCK_STREAM)
host='localhost'
port=8040
s.bind((host,port))
s.listen(4)
while True:
	c,addr=s.accept()
	data=c.recv(1024)
	match=re.search(r'GET\s/([\w.]+)',data)
#	c.send(open(match.group(1)).read())
	c.send('HTTP/1.0 200 OK \r\n')
	c.send('Content-Type: text/html\r\n\r\n')
	c.send(open(match.group(1)).read())
	c.close()
