from socket import *
s=socket(AF_INET,SOCK_STREAM)

host="127.0.0.1"
port=7003
s.bind((host,port))
s.listen(5)
client,address =s.accept()
print("connection from",address[0])

while True:
    recieved_data=client.recv(2048)
    if recieved_data.decode('utf-8') =='q':
        break
    print("client:",recieved_data.decode('utf=8'))
    
    send_data=input("server: ")
    client.send(send_data.encode("utf=8"))
    if send_data == 'q':
        break
s.close()