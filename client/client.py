import os
import socket

host, port = '127.0.0.1', 8080
host1, port1 = '0.0.0.0', 8000

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.connect((host, port))

file = open('shahid_beheshti.png', 'wb')

data = mysocket.recv(1024)

while data != bytes(''.encode()):
    # print(data)
    file.write(data)
    data = mysocket.recv(1024)

file.close()

print('file recived successfully', 'now checking the progress...')

mysocket.close()

os.system('sha1sum shahid_beheshti.png > .hash.sha1')

my_socket = socket.socket()
my_socket.connect((host1, port1))

data = str(my_socket.recv(1024).decode('utf-8'))
with open('.hash.sha1', 'r') as hash_file:
    hashData = str(hash_file.read())
    if hashData == data:
        print('File transvered without damage and error')
    else:
        print('File transvered but some error occurred')
        print('data from server :', data)
        print('hash data of transfered file :', hashData)

my_socket.close()
