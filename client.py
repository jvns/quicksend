#!/usr/bin/env python2

import socket
import sys

def get_servername(client):
    client.send("GET /servername\n\n")
    return client.recv(100000)

def send_file(client, filename):
    with open(filename) as f:
        contents = f.read()
    request = ""
    request += "PUT %s HTTP/1.1\n" % filename
    request += "Content-Length: %d\n\n" %len(contents)
    request += contents
    request += '\n'
    with open('/tmp/request.txt', 'w') as r:
        r.write(request)
    with open('/tmp/request.txt') as r:
        request = r.read()
        
    client.send(request)

if __name__ == "__main__":
    client = socket.socket()
    ip = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    client.connect((ip, port))
    print(get_servername(client))
    send_file(client, filename)
    pass

