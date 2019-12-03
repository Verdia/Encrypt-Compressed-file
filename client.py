import socket, zlib, sys
from cryptography.fernet import Fernet

host = socket.gethostname()
port = 3128

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
print("connected to the server")

# Encrypting file #
# get the key from keygen.py
keyF = open('key.key', 'rb')
key = keyF.read()
keyF.close()

# Starting to encrypt #
with open('test.mp4', 'rb') as k:
	data = k.read()
caesar = Fernet(key.decode())
encrypted = caesar.encrypt(data)
print("Done encrypting")

# Saving encrypted file #
with open('test.enc', 'wb') as j:
	j.write(encrypted)
print("Done saving the encrypted file")

# Compressing file #
file = open('test.enc', 'rb').read()
print("Raw size :", sys.getsizeof(file)/1000000, "MB")
compressed = zlib.compress(file, 9)
print("compressed size :", sys.getsizeof(compressed)/1000000, "MB")
print("Done compressing")

# Saving compressed file #
save = open('test_compressed.zip', 'wb')
save.write(compressed)
save.close()
print("Done saving the compressed file")

# Sending the file to server #
files = open('test_compressed.zip', 'rb')
file_data = files.read(1500)
while (file_data):
	s.send(file_data)
	file_data = files.read(1500)
files.close()
print("Data has been transmitted succesfully")
      
s.close()
