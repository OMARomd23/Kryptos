## Kryptos
This a harmless ransomware i made during my ransomware cybersecurity project.

The ransomware generates RSA key pairs and a random key for file encryption, sends private key to the server and  deletes it, encrypts files and the random key.

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
