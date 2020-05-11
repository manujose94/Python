#!/usr/bin/env python3
import sys, os, socket

import socketserver

import os
import sys
import webbrowser

#Python is compatible with both python version 2.7 and 3

try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3.x
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

HOSTNAME = socket.gethostname()
HOST='0.0.0.0'
'''
PORT IN USE
Command line:
    lsof -i :8005
    sudo kill -9 PID
'''
def is_port_in_use(port):
    import socket
    print(sys.version_info[0])
    if sys.version_info[0] > 2:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    else:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result= s.connect_ex(('localhost', port)) == 0
        s.close()
        return result


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

'''
This sets the listening port, default port 8005
'''
if sys.argv[1:]:
    address = sys.argv[1]
    if (':' in address):
        HOST = address.split(':')[0]
        PORT = int(address.split(':')[1])
    else:
        HOST = '0.0.0.0'
        PORT = int(address)
else:
    PORT = 8005
    HOST = '0.0.0.0'

if sys.argv[2:]:
    os.chdir(sys.argv[2])

'''
This sets the working directory of the HTTPServer, defaults to directory where script is executed.

Usage: python3 serverhttp_multithread.py [interface]:[port] [/path/to/share]

Default: [interface]:[port] = 0.0.0.0:8005

'''
if __name__=='__main__':
    if sys.argv[2:]:
        os.chdir(sys.argv[2])
        CWD = sys.argv[2]
    else:
        web_dir = os.path.join(os.path.dirname(__file__), './www') #in sever : /usr/local/bin/
        os.chdir(web_dir)
        CWD = './www'
    #Must be alllowed reuse addres
    socketserver.TCPServer.allow_reuse_address = True
    if is_port_in_use(PORT):
         print ('Port', PORT, 'already in use')
    else:
        try:
            #print(is_port_in_use(PORT))
            server = ThreadingSimpleServer((HOST, PORT), SimpleHTTPRequestHandler)
            server.allow_reuse_address = True
            cwd = os.getcwd()
            URL = "http://%s:%s"%(HOST,PORT)

            print("[OUTPUT] Serving HTTP traffic from", CWD, "on", HOSTNAME, "using port", PORT)
            print("[OUTPUT]",URL)
            webbrowser.open(URL)
            while 1:
                sys.stdout.flush()
                server.handle_request()
        except KeyboardInterrupt:
            print("[OUTPUT] Caught KeyboardInterrupt, terminating http server")
            print("\nShutting down server per users request.")
            print('[OUTPUT] stopping server on port {}'.format(server.server_port))
            import threading
            assassin = threading.Thread(target=server.shutdown)
            assassin.daemon = True
            assassin.start()
# SSL: https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python/51559006#51559006            
        

