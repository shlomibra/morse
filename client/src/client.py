import socket
PORT = 11113
BUFFER_SIZE = 1024
with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect (('172.17.0.1', PORT))
    print (s.recv (BUFFER_SIZE) .decode ())
