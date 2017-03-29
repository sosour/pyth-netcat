#!/usr/bin/python
import sys
import socket
import getopt
import threading
import subprocess
import globals
from client_server import *

def usage():
    print "NETKOT"
    print
    print "Usage: netkot.py -t target_host -p port"
    print "-l --listen			listen on [host]:[port]"
    print "-e --execute=file_to_run	execute file on connection"
    print "-c --command			initializes command line"
    print "-u --upload=destination	uploads file to destination"
    print
    print
    print "Example usage:"
    print "netkot.py 192.168.0.1:9999 -l -c"
    print "netkot.py 192.168.0.1:9999 -l -u=C://target.exe"
    print "netkot.py 192.168.0.1:9999 -l -e \"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./netkot.py -t 192.168.11.12:135"
    sys.exit(0)

def main():
    globals.initg()
    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:",
        ["help","listen","execute","target","port","command","upload"])  
    except getopt.GetoptError as err:
        print str(err)
        usage()  
    
    for o,a in opts:
        if o in ("-h", "--help"):
	        usage()
        elif o in ("-l", "--listen"):
            globals.listen = True
        elif o in ("-e", "--execute"):
            globals.execute = a
        elif o in ("-t", "--target"):
	        globals.target = a
        elif o in ("-p", "--port"):
            globals.port = int(a)
        elif o in ("-c", "--command"):
      	    globals.command = a
        elif o in ("-u","--upload"):
            globals.upload_destination = a
        else:
	        assert False,"Unsupported option"

    if not globals.listen and len(globals.target) and globals.port > 0:
        buffer = sys.stdin.read()
        
        client_sender(buffer)

    if globals.listen:
        server_loop()

main()
