#!/usr/bin/env python3
import socket
import json

def start_server():
    """Start the server that listens for client connections and processes received data."""
    # Set up the server socket
    host = '127.0.0.1'  # Localhost
    port = 12345  # Arbitrary port number
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the server socket to the address and port
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Server listening on {host}:{port}...")

    # Accept incoming connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    try:
        # Receive the data from the client (up to 1024 bytes)
        data = client_socket.recv(1024)
        
        if data:
            # Deserialize the received data using JSON
            received_dict = json.loads(data.decode())
            print("Received Dictionary from Client:")
            print(received_dict)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client connection
        client_socket.close()
        print("Connection closed.")

