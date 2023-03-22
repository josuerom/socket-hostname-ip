import socket
import random

def server_program():
    # get the hostname
    host = "172.18.0.2"
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn1, address1 = server_socket.accept()  # accept first connection
    print("Se ha establecido conexion con el cliente 1: " + str(address1))
    conn2, address2 = server_socket.accept()  # accept second connection
    print("Se ha establecido conexion con el cliente 2: " + str(address2))

    # generate and send unique random numbers to each client
    numbers = random.sample(range(1, 11), 10)
    conn1.send(str(numbers).encode())
    print("Numeros aleatorios enviados a cliente 1")
    conn2.send(str(numbers).encode())
    print("Numeros aleatorios enviados a cliente 2")

    # receive remaining numbers from clients and sort the list
    received1 = conn1.recv(1024).decode()
    received2 = conn2.recv(1024).decode()
    remaining1 = [int(num) for num in received1.split(',') if num not in received2]
    remaining2 = [int(num) for num in received2.split(',') if num not in received1]
    numbers = sorted(remaining1 + remaining2)

    # send sorted list to clients
    conn1.send(str(numbers).encode())
    conn2.send(str(numbers).encode())

    conn1.close()  # close the first connection
    conn2.close()  # close the second connection

    f = open('output.txt', 'a')
    f.write('IP Cliente 1: ' + str(address1) + '\n')
    f.write('IP Cliente 2: ' + str(address2) + '\n')
    
if __name__ == '__main__':
    server_program()
