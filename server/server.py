import os
import socket

host, port = '127.0.0.1', 8080

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
    flag = False
    while data != bytes(''.encode()):
        left = file_size - 1024 * counter
        if left > 0:
            print(int(((1024 * counter) / file_size) * 100), '% Completed')
        else:
            print('File transfering over.')
            flag = True
        s.send(data)
        if flag:
            s.send('\n\n'.encode('utf-8'))
        data = file.read(1024)
        counter += 1
    print('File sent successfully.')

with open('.hash.sha1', 'r') as hash_file:
    data = str(hash_file.read())
    print('data to send :', data)
    s.send(data.encode('utf-8'))

print('everything done sucsessfully\nclosing socket')

s.close()
