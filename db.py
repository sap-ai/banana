import socket
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    headers = request.split('\n')
    try: filename = headers[0].split()[1]
    except: filename = ""
    mf = filename.split("%")
    if len(mf) == 2:
        with open("db.txt", 'a') as file:
           file.write(mf[1])
    r = open("db.txt")
    response = 'HTTP/1.0 200 OK\n\n' + r.read()
    client_connection.sendall(response.encode())
    client_connection.close()
server_socket.close()
