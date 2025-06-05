import socket
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
while True:
    p = open("db.txt")
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    headers = request.split('\n')
    try: filename = headers[0].split()[1]
    except: filename = ""
    if filename == "sz": response = p.read()
    else:
          with open("db.txt", 'w') as file: file.write(filename[1: len(filename)+1])
    client_connection.sendall(response.encode())
    client_connection.close()
server_socket.close()
