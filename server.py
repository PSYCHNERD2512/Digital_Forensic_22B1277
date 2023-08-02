import socket
import random
import string


server_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


ip_address = '127.0.0.1'
port = 5555
server_object.bind((ip_address, port))
server_object.listen()


connection_object, _ = server_object.accept()


if connection_object:

    print("SERVER CONNECTED TO CLIENT")

    connection_object.send(b"type the message")

    data_receive = connection_object.recv(1024)
    
    while data_receive != b'stop':
        print("{}: {}".format("CLIENT MESSAGE: ", data_receive.decode('utf-8')))
        server_input = random.choice(string.ascii_letters)
        connection_object.send(server_input.encode('utf-8'))
        data_receive = connection_object.recv(1024)