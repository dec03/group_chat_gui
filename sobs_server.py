import socket
import _thread
import threading


def on_new_client(client_ip,client_address):
    while True:
        data = client_ip.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        index = clients.index(client_ip)

        m = f'{client_name[index]}: '
        data = m + data
        for i in clients:
            i.send(data.encode())

        print(f"from connected {str(data)}")
        if data.lstrip() == 'bye':
            print(f'{client_name[index]} has disconnected')
            for i in clients:
                i.send(f'{client_name[index]} has disconnected'.encode())

    client_ip.close()


clients = []
client_name = []

# get the hostname
host = socket.gethostname()
port = 12345  # initiate port no above 1024

server_address = host

server_socket = socket.socket()  # get instance
# look closely. The bind() function takes tuple as argument
server_socket.bind((host, port))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen()



while True:
    conn, client_address = server_socket.accept()  # accept new connection
    c_name = conn.recv(1024).decode()
    client_name.append(c_name)

    print(f'{client_address}/: {c_name} connected')
    _thread.start_new_thread(on_new_client,(conn,client_address))
    clients.append(conn)
    for i in clients:
        i.sendall(f'{client_address} Connected to server'.encode())


conn.close()  # close the connection
