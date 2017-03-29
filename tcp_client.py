#!/usr/bin/python
import socket
import sys

target_host, target_port = str(sys.argv[1]).split(":") 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, int(target_port)))

client.send("GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % target_host)

response = client.recv(4096)

print response

