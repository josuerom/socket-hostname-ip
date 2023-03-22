import socket

def server_program():
    # get the hostname
    host = "172.18.0.2"
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Se ha establecido conexion con el cliente: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Respuesta del cliente: " + str(data))
        data = input('--> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

    f = open('output.txt', 'a')
    f.write('IP: ' + str(address) + '\n')
    #f.close()

if __name__ == '__main__':
    server_program()
