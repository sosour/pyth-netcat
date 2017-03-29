#!/usr/bin/python
import sys
import socket
import getopt
import threading
import subprocess

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
    print "Usage: netkot.py target_host:port"
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
    usage()

main()
