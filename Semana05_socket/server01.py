import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)


nome_do_arquivo_original = input('Digite o nome do arquivo a ser enviado:')
arquivo = open('nome_do_arquivo_original','r')
while True:
  
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida.")


    arq = pickle.dumps(arquivo)
    arq = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+arq

    clientsocket.send(arq)
