import socket

# создаем серверный сокет:

serv_sock = socket.socket(socket.AF_INET,     #задаем семейство протоколов "Интернет" (INET)
                          socket.SOCK_STREAM, #задаем тип передачи данных "потоковый" (TCP)
                          proto=0             #выбираем протокол по умолчанию для TCP, т.е. IP
                          )

print(type(serv_sock))

HOST = '127.0.0.1'
PORT = 53210


serv_sock.bind(HOST,PORT)# привязываем созданные сокет к сетевому адаптеру
backlog = 10#Размер очереди входящих подключений
serv_sock.listen(backlog)
client_sock,client_adr = serv_sock.accept()#получаем соединение из очереди клиентов 
print('Connected by',client_adr)

# Чтение и запись в клиентский сокет:

while True:
    data = client_sock.recv(1024)
    if not data:
        break
    client_sock.sendall(data)

client_sock.close()







