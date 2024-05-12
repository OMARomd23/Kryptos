from cryptography.fernet import Fernet
import rsa
import base64
import os


def key_decryptor():
    path=input("enter full path of the private key: ")
    path2=[]
    for y in path:
        if y == "\\":
            path2.append("/")
        else:
            path2.append(y)
    path=''.join(path2)

    with open(path, 'rb') as pvkey:
        privateKey = rsa.PrivateKey.load_pkcs1(pvkey.read())
    with open("encrypted_key.ekey",'rb') as enctd_ekey:
        encrypted_enc_key=enctd_ekey.read()
    return rsa.decrypt(base64.b64decode(encrypted_enc_key), privateKey).decode('utf-8')


def file_decryptor():
    username = os.getlogin()
    path = f'C:/Users/{username}/Documents'
    fernet_dec=Fernet(key_decryptor())
    ls=os.listdir(path)
    files=[x for x in ls if '.enctd' in x]
    for i in files:
        with open(f'{path}/{i}','rb') as encptd_file:
            ciphertxt=encptd_file.read()
        decrypted_data=fernet_dec.decrypt(ciphertxt)
        with open(f"{path}/decrypted_{i.split('-')[1]}", 'wb') as dfile:
            dfile.write(decrypted_data)
        os.remove(f'{path}/{i}')
file_decryptor()
