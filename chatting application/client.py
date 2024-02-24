# import required modules
import socket
import threading

# main function
def main():

    # creating a socket object
    client = socket.socket(socket.AF_inet, socket.SOCK_STREAM)

    # connect to the server
    try:
        client.connect((HOST, PORT))
        print(F"Sucessfully connected to the server")
    except:
        print(f"Unable to connect to the server {HOST} {PORT}")

if__name__=='__main__':
    main()
