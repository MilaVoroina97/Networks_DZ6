import socket, threading


# Открываем сокет
sock = socket.socket()

HOST = '127.0.0.1'
PORT = 53210

# Коннектимся

sock.connect(HOST,PORT)

# Подготовим HTTP-запрос
def sock_send(data):
    sock.send(data)

def sock_recieve():
# Передаём размер буфера - по сколько байт будем перехватывать с нашей сетевой карты приходящих на неё данных и заносить в переменную
    while True:
        data_in = sock.recv(1024)
        print(data_in.decode('ascii'))

sock_send(b"mila")

rec_thread = threading.Thread(target=sock_recieve)
rec_thread.start()

while True:
    data = input()
    sock_send(f"mila: {data}".encode('ascii'))
