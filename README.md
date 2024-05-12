## Kryptos
This a harmless ransomware i made during my ransomware cybersecurity project.
The ransomware generates RSA key pairs and a random key for file encryption and  encrypts it with the public key generated, sends private key to the server and  deletes it and encrypts files with the random generated key.

## Requirements
Before running the ransomware, make sure these packages are installed:

  - [Cryptography](https://pypi.org/project/cryptography/)
  - [RSA](https://pypi.org/project/rsa/)
  - [Colorama](https://pypi.org/project/colorama/)
 

You will also need to change the ip address on the [client_key_sender.py](https://github.com/OMARomd23/Kryptos/blob/main/client_key_sender.py) file to match the server's ip.

And then run the [server.py](https://github.com/OMARomd23/Kryptos/blob/main/server.py) Before [KRYPTOS.py](https://github.com/OMARomd23/Kryptos/blob/main/KRYPTOS.py).

# How does  the ransomware work step by step:

	1. It generates RSA key pairs
	
	2. Sends the private key to the server and deletes it from the victim's machine.
	
	3. Generates a random key for encryption.
	
	4. Encrypts the random key and stores it on a file.
	
	5. Locates all the files ending with  (".txt", ".png", ".pdf", ".jpg")
	
# How does the decryptor work:

 Before you can use the decryptor you need to have the private key which is sent to the server during the encryption.


	1. It firsts uses the private key to decrypt the encryption key stored on "encrypted_key.ekey" file.
 	
  	2. Then lists all the files ending with ".enctd" which are the files that are encrypted.
	
	3. Decrypts each of the encrypted files and name them 'decrypted_[old file name].
 
	4. Deletes the encrypted files.
