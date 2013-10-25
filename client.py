#!/usr/bin/env python2

import socket
import sys

def get_servername(client):
    client.send("GET /servername\n\n")
    return client.recv(100000)

def send_file(client, filename):
    with open(filename) as f:
        contents = f.read()
    client.send("PUT %s HTTP/1.1\n" % filename)
    client.send("Content-Length: %d\n\n", len(contents))
    client.send(contents)

if __name__ == "__main__":
    client = socket.socket()
    client.connect(('127.0.0.1', 8000))
    print(get_servername(client))
    send_file(client, '/tmp/testfile')
    pass

