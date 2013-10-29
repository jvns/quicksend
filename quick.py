#!/usr/bin/env python2

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

DEFAULT_PORT=12345

def print_help():
    print """Usage:

To receive files:
$ quick receive [port]

To send files: 
$ quick send hostname [port]

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
    server_address = ('localhost', port)
    server = HTTPServer(server_address, QuickServerRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    print_help()
    start_server(DEFAULT_PORT)

