import os
import socket

host, port = '127.0.0.1', 8080

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.connect((host, port))

file = open('shahid_beheshti.png', 'wb')

print('start reciving file ...')

first_data = mysocket.recv(256)

data = mysocket.recv(int.from_bytes(first_data, 'big'))

file.write(data)

file.close()

print('file recived successfully', 'now checking the progress...')

os.system('sha1sum shahid_beheshti.png > .hash.sha1')
print()

file_code = mysocket.recv(256).decode('utf-8')

with open('.hash.sha1', 'r') as hash_file:
    hashData = hash_file.read()
    if hashData == file_code:
        print('File transvered without damage and error')
    else:
        print('File transvered but some error occurred')
        print('data from server :', file_code)
        print('hash data of transfered file :', hashData)

mysocket.close()
