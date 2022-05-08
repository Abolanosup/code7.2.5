from telegram.ext import Updater

import random 
from tcping import Ping
import ping3   
import socket 
import telegram 
import S5Crypto

def Search_ping():
    print("Buscando proxy...")
    for port in range(2080,2085): # El rango del puerto
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = sock.connect_ex(('181.225.253.188',port)) # IP o dirección,puerto o poner la variable port para escanear los puertos

        if result == 0: # Si el puerto está activo
            print ("Puerto abierto!")
            print (f"Puerto: {port}")  
            proxy = f'181.225.253.188:{port}'
            proxy_new = S5Crypto.encrypt(f'{proxy}')
            break
        else: # Si hay error hal escanear un puerto
            print ("Error...Buscando...")
            print (f"Buscando en el puerto: {port}")
            sock.close()

# Ejemplo de como usar mi módulo:
# print(porxy)

# De donde a donde se va a escanear
# for port in range()

       
                
                
        
        
     
        
            
     
