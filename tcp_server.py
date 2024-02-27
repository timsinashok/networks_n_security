import socket

def start_server(host, port):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the host and port
        server_socket.bind(('0.0.0.0', port))
        
        # Start listening for incoming connections
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        # Accept incoming connections
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Process the received data (you can customize this part)
            print(f"Received data: {data.decode()}")

            # Send a response back to the client (optional)
            response = "Hello from server"
            client_socket.sendall(response.encode())

            # Close the connection with the client
            client_socket.close()

if __name__ == "__main__":
    # Set the host and port for the server
    HOST = '##ip###'  # Change to your laptop's IP address if needed
    PORT = 1239  # Choose any available port

    start_server(HOST, PORT)
