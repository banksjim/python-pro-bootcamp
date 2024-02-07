import socket

# Define the host and port of the TCP server
HOST = '127.0.0.1'  # Loopback address for localhost
PORT = 12345        # Same port as the TCP server

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    
    # Send data to the server
    message = "Hello, TCP server!"
    client_socket.sendall(message.encode())
    print(f"Sent: {message}")

    # Receive data from the server
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
