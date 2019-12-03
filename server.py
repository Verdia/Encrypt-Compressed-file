import socket, zlib, sys
from cryptography.fernet import Fernet

host = '192.168.43.101'
port = 3128

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

file = open('output/test_compressed.zip', 'wb')

# Recv file from client #
conn,addr = s.accept()
print("Get connection with ",addr)
file_data = conn.recv(1500)
while(file_data):
	file.write(file_data)
	file_data = conn.recv(1500)
file.close()
print("File has been received")

# Decompressing file #
files = open('output/test_compressed.zip', 'rb').read()
decomp = zlib.decompress(files)

# Saving decompressed file #
save = open('output/test.enc', 'wb')
save.write(decomp)
save.close()
print("Done decompressing the file")

# Decrypting file #
# get the key from keygen.py
keyF = open('key.key', 'rb')
key = keyF.read()
keyF.close()

# Starting to decrypt #
with open('output/test.enc', 'rb') as e:
	data = e.read()
caesar = Fernet(key)
dec = caesar.decrypt(data)

# Saving decrypted file #
with open('output/test.jpg', 'wb') as f:
	f.write(dec)
f.close
print("Done decrypting the file")
