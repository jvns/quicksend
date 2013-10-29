#!/usr/bin/env python2

import socket
import sys

def get_servername(client):
    client.send("GET /servername\n\n")
    return client.recv(100000)

def create_put_request(filename):
    with open(filename) as f:
        contents = f.read()
    request = ""
    request += "PUT %s HTTP/1.1\n" % filename
    request += "Content-Length: %d\n\n" %len(contents)
    request += contents
    request += '\n'
    return request

def send_file(ip, port, filename):
    sock = socket.socket()
    sock.connect((ip, port))
    request = create_put_request(filename)
    sock.send(request)
    sock.close()

if __name__ == "__main__":
    ip, port, filename = sys.argv[1:4]
    port = int(port)
    send_file(ip, port, filename)
