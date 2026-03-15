import socket

host = "127.0.0.1"
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Server started. Waiting for connection...")

conn, addr = server.accept()
print("Connected with", addr)

while True:
    message = conn.recv(1024).decode()
    print("Client:", message)

    reply = input("You: ")
    conn.send(reply.encode())