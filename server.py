'''
    Simple socket server using threads
'''
 
import socket
import sys
 
HOST = '192.168.1.10'   # Symbolic name, meaning all available interfaces
PORT = 55535 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
#data = s.recv(2048)
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    d = conn.recv(2048)
    print('*'*20)
    print(d)
    print('*'*20)

s.close()
