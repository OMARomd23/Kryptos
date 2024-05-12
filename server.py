import time
import socket 

host=''
info_port=9090
key_port = 6009

def recieving_info():
    global file_name
    global file_size
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as info_soc:
        info_soc.bind((host, info_port))
        info_soc.listen()
        client_info, addr = info_soc.accept()

        print('Recieved A Connection From ', addr)

        print('recieving file name')
        file_name = client_info.recv(1024).decode()
        print("the file will be saved as ",file_name)
        time.sleep(1)

        print("recieving file size...")
        file_size = client_info.recv(1024).decode()

    print("the file is ",file_size, " bytes")

def recieving_key():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as key_soc:
        key_soc.bind((host, key_port))
        key_soc.listen()
        client_key, addr = key_soc.accept()
        print("Recieving the key...")
        key_bytes = b""

    done = False
    
    while not done:
        key= client_key.recv(1024)
        if not key:
            done = True
        else:
            key_bytes += key
    with open(file_name, 'wb') as the_key:
        the_key.write(key_bytes)


if __name__ == "__main__":
    recieving_info()
    recieving_key()
            

