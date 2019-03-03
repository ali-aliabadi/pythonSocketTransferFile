import os
import socket

host, port = '127.0.0.1', 8080

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.connect((host, port))

file = open('shahid_beheshti.png', 'wb')

data = mysocket.recv(1024)
data1 = ''

departed = len('\n\n')
flag = False

while data != bytes(''.encode()):
    for i in range(1024 - departed):
        if '\n\n'.encode('utf-8') == data[i:i + departed:]:
            data1 = data[i+departed::].decode('utf-8')
            data = data[:i:]
            flag = True
    file.write(data)
    data = mysocket.recv(1024)
    if flag:
        if len(data.decode('utf-8')):
            data1 += data.decode('utf-8')
        break

file.close()

print('file recived successfully', 'now checking the progress...')

os.system('sha1sum shahid_beheshti.png > .hash.sha1')
print()

with open('.hash.sha1', 'r') as hash_file:
    hashData = str(hash_file.read())
    if hashData == data1:
        print('File transvered without damage and error')
    else:
        print('File transvered but some error occurred')
        print('data from server :', data1)
        print('hash data of transfered file :', hashData)

mysocket.close()
