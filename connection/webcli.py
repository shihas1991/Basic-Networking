import socket
s=socket.socket()
host="localhost"
port=8010
s.connect((host,port))
s.close()
