#!/usr/bin/python

def client_sender(buffer):
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


def server_loop():
    global target

    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)


    while True:
	client_socket, addr = server.accept()

	client_thread = threading.Thread(target=client_handler, args=(client_socket,))
	client_thread.start()

def run_command(command):
    command = command.rstrip()
    try:
	output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
	output = "Failed to execute the command\r\n"
    return output

def client_handler(client_socket):
    global uplaod
    global execute
    global command
    
    if len(upload_destination):
            file_buffer = ""

            while True:
                data = client.socket.recv(1024)

                if not data:
                    break
                else:
                    file_buffer += data
            try:
                file_descriptor = open(upload_destination, "wb")
                file_descriptor.write(file_buffer)
                file_descriptor.close()

                client_socket.send("File saved in %s\r\n" % upload_destination)
            except: client_socket.send("Failed to save file to %s\r\n" % upload_destination)

    if len(execute):
        output = run_command(execute)
        client_socket.send(output)

    if command:
        while True:
            client_socket.send("NETKOT:# ")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            response = run_command(cmd_buffer)

            client_socket.send(response)
