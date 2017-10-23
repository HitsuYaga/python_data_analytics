import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('222.255.102.149', 5045)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

message = 'This is the message.  It will be repeated.'
print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)

sock.close()