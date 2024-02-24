# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234 # You can use any port between 0 to 65535

# Main function
def main():
    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket>SOCK_STREAM)

    # Create a try catch block
    try:
        # Provide the server with an adress in the form of
        # Host IP and Port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {port}")
    except:
            print(f"Unable to bind to host {HOST} and {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)

    # This loop will keep listening to client connections
    while 1:

        client, address = server.accept()
        print(f"Successfully connect to client {address[0]} {address[1]}")
        
if __name__=='__main__':
