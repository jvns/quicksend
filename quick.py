#!/usr/bin/env python2

# How to bundle together the server name?

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

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
            self.send_error(411)

        with open(filename, 'w') as out:
            content_length = int(self.headers['content-length'])
            out.write(self.rfile.read(content_length))


    def send_servername(self):
        name = "Julia\n"
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", str(len(name)))
        self.wfile.write(name)

# class QuickServer(HTTPServer):
#     def __init__(self, server_address):
#         super(self, server_address, QuickServerRequestHandler)

if __name__ == "__main__":
    server_address = ('', 8000)
    server = HTTPServer(server_address, QuickServerRequestHandler)
    server.serve_forever()

