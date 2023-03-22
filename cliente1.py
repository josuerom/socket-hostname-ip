import socket

# Datos del servidor
host = '172.18.0.2'
port = 5000

# Función para recibir números faltantes de otros clientes
def receive_missing_nums(client_socket):
    data = client_socket.recv(1024).decode()
    return eval(data)

# Función principal del cliente
def client_program():
    # Crear socket del cliente y conectarse al servidor
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    # Recibir números aleatorios del servidor
    data = client_socket.recv(1024).decode()
    nums = eval(data)
    
    # Inicializar lista de números del cliente
    client_nums = []
    
    # Mientras el cliente no tenga todos los números, seguir recibiendo
    while len(client_nums) < 11:
        # Enviar números actuales al servidor y recibir números faltantes
        client_socket.send(str(client_nums).encode())
        missing_nums = receive_missing_nums(client_socket)
        
        # Actualizar lista de números del cliente y ordenarla
        client_nums += missing_nums
        client_nums = list(set(client_nums))
        client_nums.sort()
    
    # Enviar lista completa al servidor y cerrar conexión
    client_socket.send(str(client_nums).encode())
    client_socket.close()

# Iniciar programa
if __name__ == '__main__':
    client_program()
