#!/usr/bin/python

def client_sender(buffer, target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
	client.connect((target,port))
	if len(buffer):
	    client.send(buffer)

	while True:

	    recv_len = 1
	    response = ""

	    while recv_len:

		data = client.recv(4096)
		recv_len = len(data)
		response += data

		if recv_len < 4096:
		    break

	    print response,

	    buffer = raw_input("")
	    buffer += "\n"

	    client.send(buffer)

    except:
	print "Exception! Closing"
	
	client.close()
