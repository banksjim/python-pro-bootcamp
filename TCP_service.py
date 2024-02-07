import socket

# Define the host and port for the service
HOST = '127.0.0.1'  # Loopback address for localhost
PORT = 12345        # Arbitrary port number

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections
    server_socket.listen()

    print(f"TCP server is listening on {HOST}:{PORT}")
    
    # Accept incoming connections
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    with conn:
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")

            # Echo the received data back to the client
            conn.sendall(data)
