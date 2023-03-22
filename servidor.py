import socket
import threading
import random

# Datos del servidor
host = '172.18.0.2'
port = 5000
max_clients = 2

# Datos del juego
nums = list(range(11))
random.shuffle(nums)

# Lista de clientes conectados
clients = []

# Función para enviar mensaje a todos los clientes
def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

# Función para atender a cada cliente
def handle_client(client):
    # Agregar cliente a la lista
    clients.append(client)
    
    # Enviar números aleatorios al cliente
    client.send(str(nums).encode())
    
    # Recibir números del cliente
    data = client.recv(1024).decode()
    client_nums = eval(data)
    
    # Mientras el cliente no tenga todos los números, seguir recibiendo
    while len(client_nums) < 11:
        data = client.recv(1024).decode()
        new_nums = eval(data)
        
        # Enviar números faltantes al cliente y actualizar lista
        missing_nums = list(set(nums) - set(client_nums))
        new_nums = list(set(new_nums) - set(client_nums))
        client.send(str(new_nums).encode())
        client_nums += new_nums
        
        # Si hay números faltantes, pedirlos a otro cliente
        if len(missing_nums) > 0:
            broadcast(str(missing_nums).encode(), client)
            data = client.recv(1024).decode()
            new_nums = eval(data)
            client_nums += new_nums
    
    # Ordenar y enviar lista completa al cliente
    client_nums.sort()
    client.send(str(client_nums).encode())
    
    # Cerrar conexión
    clients.remove(client)
    client.close()

# Función principal del servidor
def server_program():
    # Crear socket del servidor
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(max_clients)
    
    print('Servidor iniciado. Esperando conexiones...')
    
    # Ciclo para atender a todos los clientes
    while True:
        client, address = server_socket.accept()
        print('Nueva conexión establecida:', address)
        t = threading.Thread(target=handle_client, args=(client,))
        t.start()

# Iniciar programa
if __name__ == '__main__':
    server_program()
