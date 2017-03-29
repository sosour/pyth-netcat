#!/usr/bin/pyton
import socket
import threading
import globals

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((globals.target, globals.port))

        if len(buffer):
            client.send(buffer)

        while True:

            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                print data
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                   break

            print response
            buffer = raw_input("")
            buffer += "\n"
            client.send(buffer)

    except:
	    print "Exception! Closing"
	
	    client.close()


def server_loop():

    if not len(globals.target):
        globals.target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((globals.target, globals.port))
    server.listen(5)
    print "Listening on %s:%s" % (globals.target, str(globals.port))

    while True:
        client_socket, addr = server.accept()
        print client_socket
        print addr
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
    
    if len(globals.upload_destination):
            file_buffer = ""

            while True:
                data = client.socket.recv(1024)

                if not data:
                    break
                else:
                    file_buffer += data
            try:
                file_descriptor = open(globals.upload_destination, "wb")
                file_descriptor.write(file_buffer)
                file_descriptor.close()

                client_socket.send("File saved in %s\r\n" % globals.upload_destination)
            except: 
                client_socket.send("Failed to save file to %s\r\n" % globals.upload_destination)

    if len(globals.execute):
        output = run_command(globals.execute)
        client_socket.send(output)

    if globals.command:
        while True:
            client_socket.send("<NETKOT:#>")
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            response = run_command(cmd_buffer)
            print "Sending response"
            client_socket.send(response)
