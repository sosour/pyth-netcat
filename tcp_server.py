import socket
import threading 
import sys

bind_ip, bind_port =  str(sys.argv[1]).split(":")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, int(bind_port)))

server.listen(5)

print "Listening on %s:%s" % (bind_ip, bind_port)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "Received request: %s" % request
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr = server.accept()
    print "Connection accepted from %s:%d" % (addr[0], addr[1])	
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
