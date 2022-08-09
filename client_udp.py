import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Mensagem: ") + "\n"
    client.sendto(msg.encode(), ("127.0.0.1", 999))
    data, sender = client.recvfrom(1024)

    client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client2.bind(("127.0.0.1", 444))
    msg, send = client2.recvfrom(1024)
    print(send[0] + ": " + msg.decode())
    client2.sendto(msg,send)
    


    


