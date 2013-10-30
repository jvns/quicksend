#!/usr/bin/env python2

import sys

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

DEFAULT_PORT=12345

def print_help():
    print """Usage:

To receive files:
$ quick receive [port]

To send files: 
$ quick send hostname filename [port]

The default port is %d.
""" % DEFAULT_PORT


class QuickServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path == "/servername":
            self.send_servername()

    def do_PUT(self):
        # Just take the last element of the path
        filename = self.path.split('/')[-1]

        if 'content-length' not in self.headers:
            # 411 is "Content-Length not defined"
            self.send_response(411)
            self.send_error(411)
            return

        print "Receiving file %s... " % filename,
        with open(filename, 'w') as out:
            content_length = int(self.headers['content-length'])
            out.write(self.rfile.read(content_length))
        print "Done!"


    def send_servername(self):
        name = "Julia\n"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", str(len(name)))
        self.wfile.write(name)

def start_server(port):
    print "Waiting for files on port %d...\n" % port
    server_address = ('localhost', port)
    server = HTTPServer(server_address, QuickServerRequestHandler)
    server.serve_forever()

def parse_args(args):
    if len(args) == 0:
        return
    action = args[0]
    if action == 'receive':
        port = args[1] if len(args) >= 2 else DEFAULT_PORT
        return {'action': 'receive', 'port': port}
    elif action == 'send':
        if len(args) <= 2:
            print "Not enough arguments for 'send'."
            return
        hostname, filename = args[1:3]
        port = DEFAULT_PORT
        if ':' in hostname:
            hostname, port = machine.split(':')
        return {
            'action': 'send',
            'port': port,
            'hostname': hostname,
            'filename': filename
        }
    else:
        print "I don't know how to 'quick %s'. Sorry." % action
        return


if __name__ == "__main__":
    config = parse_args(sys.argv[1:])
    if config is None:
        # Invalid arguments
        print_help()
        sys.exit(0)
    elif config['action'] == 'receive':
        start_server(config['port'])
