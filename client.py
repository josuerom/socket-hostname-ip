import socket

def client_program():
    host = "172.18.0.2"
    port = 5000

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    username = input("Ingrese el nombre: ")
    message = input("--> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Repuesta del servidor: ' + data)  # show in terminal
        message = input("--> ")  # again take input

    client_socket.close()  # close the connection
    
    f = open('output.txt', 'w')
    f.write('Nombre del cliente: ' + username + '\n')

if __name__ == '__main__':
    client_program()
