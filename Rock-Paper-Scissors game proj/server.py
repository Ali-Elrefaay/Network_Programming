import random
import socket

HOST = 'localhost'
PORT = 65500

# Function to convert choice to a number
def choice_to_number(choice):
    rps = {'scissor': 0, 'paper': 1, 'rock': 2}
    return rps[choice]

# Creating a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Binding the socket to a specific address and port
    s.bind((HOST, PORT))
    # Listening for incoming connections
    s.listen()
    print("server is listening.......")

    # Accepting incoming connections
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # Receiving the client's choice
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break

            # Generating the computer's choice
            comp_choice = random.choice(['scissor', 'paper', 'rock'])
            conn.sendall(comp_choice.encode('utf-8'))
            