import os
import socket

host, port = '127.0.0.1', 8080
host1, port1 = '0.0.0.0', 8000

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((host, port))

print('server created')
print('waiting for client...')

my_socket.listen(1)
s, addr = my_socket.accept()
print('connection from :', str(addr))

file_size = os.path.getsize('shahid_beheshti.png')
print('file size : {}'.format(str(file_size)), 'bytes')

with open('shahid_beheshti.png', 'rb') as file:
    os.system('sha1sum shahid_beheshti.png > .hash.sha1')
    counter = 1
    data = file.read(1024)
    while data != bytes(''.encode()):
        if (1024 * counter < file_size):
            print(int(((1024 * counter) / file_size) * 100), '% Completed')
        else:
            print('File transfering over.')
        s.send(data)
        data = file.read(1024)
        # print(data)
        counter += 1
    print('File sent successfully.')

s.close()

print('server 1 deleted\ncreating server 2')

my_socket = socket.socket()
my_socket.bind((host1, port1))

print('connecting to client...')

my_socket.listen(1)
s, addr = my_socket.accept()

print('server 2 connected')

with open('.hash.sha1', 'r') as hash_file:
    data = str(hash_file.read())
    # print('data to send :', data)
    s.send(data.encode('utf-8'))

print('everything done sucsessfully\nclosing socket')

s.close()
