import socket
import sys

target_host, target_port = str(sys.argv[1]).split(":") 

message = str(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(message, (target_host, int(target_port)))

data, addr = client.recvfrom(4096)

print data

