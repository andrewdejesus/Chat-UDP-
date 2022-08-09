import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("127.0.0.1", 999))
print("Aguardando conexão")
while True:
    
    msg, client = servidor.recvfrom(1024)
    print(client[0] + ": " + msg.decode())
    servidor.sendto(msg,client)

    msg = input("Mensagem: ") + "\n"
    servidor.sendto(msg.encode(), ("127.0.0.1", 444))
    data, sender = servidor.recvfrom(1024)

   
    
    