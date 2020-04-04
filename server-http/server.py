# server.py
import webbrowser
import http.server
import socketserver
import getopt
import os
import sys
HOST = '0.0.0.0'
PORT = 8005
URL = "http://%s:%s"%(HOST,PORT)
#HOST ="158.42.163.97"
USAGE = "Usage: python {sys.argv[0]} [--help] | [-h <HOST> ] [-p <port> ]"

#
# Sample params
# /usr/bin/python3 server.py -h 127.0.0.1 -p 8081

def parse(args):
    options, arguments = getopt.getopt(
        args,                              # Arguments
        'iu:h:p:',                            # Short option definitions
        ["info","host=", "port=" ]) # Long option definitions
    global HOST
    global PORT
    for o, a in options:
        if o in ("-i", "--help"):
            print(USAGE)
        if o in ("-h", "--host"):
            print(a)
            if a != None:
                HOST = a 
        if o in ("-p", "--port"):
            print(a)
            if a != None:
                try:
                    PORT = int(a)
                except ValueError:
                    PORT = 8005
    global URL 
    URL = "http://%s:%s"%(HOST,PORT)
    print(URL)


def main():
    args = sys.argv[1:]
    parse(args)



#
# MAIN
#
if __name__=='__main__':
    main()   
    web_dir = os.path.join(os.path.dirname(__file__), './www') #in sever : /usr/local/bin/
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    # Python version 3.5 

    #Must be alllowed reuse addres
    socketserver.TCPServer.allow_reuse_address = True
    httpd  = socketserver.TCPServer(("", PORT), Handler)

    print("serving HTTP SERVER at port", PORT)
    print(URL)
    try:
       # webbrowser.open(URL)
        httpd.serve_forever()
       
    except KeyboardInterrupt:
        print("Caught KeyboardInterrupt, terminating http server")
        httpd.shutdown()
   
   

