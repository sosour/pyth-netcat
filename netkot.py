#!/usr/bin/python
import sys
import socket
import getopt
import threading
import subprocess
import client_sender

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

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
    global listen 
    global port
    global execute
    global command
    global upload_destination
    global target

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
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-t", "--target"):
	    target = a
        elif o in ("-p", "--port"):
	    port = int(a)
        elif o in ("-c", "--command"):
      	    command = a
        elif o in ("-u","--upload"):
	    upload_destination = a
	else:
	    assert False,"Unsupported option"

	if not listen and len(target) and port > 0:
	    buffer = sys.stdin.read()

            client_sender(buffer, target, port)

	if listen:
	    server_loop()


main()
