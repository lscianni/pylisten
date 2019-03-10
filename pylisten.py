#!/usr/bin/env python
#
# HTTP listener
# Louis Scianni 2/23/2018

import http.server
import socketserver
from sys import argv

def help_info():
    print('usage:%s port\nCreates a HTTP listener on the specified port' % argv[0])    
    
try:
    port = argv[1]

except IndexError:
    help_info()
    
def start_listener(port):
    server_address = ('127.0.0.1', int(port))
    handler = http.server.SimpleHTTPRequestHandler
    handler.cgi_directories = ['/cgi-bin']
    httpd = socketserver.TCPServer(server_address, handler)
    """
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('', int(port)), handler)
    """
    try:
        print("listener on %s" % port)
        httpd.serve_forever()
    except:
        print('stopping listener on %s' % port)

def main():
    start_listener(port)
    
if __name__ == '__main__':
    try:
        main()
    except NameError:
        pass
