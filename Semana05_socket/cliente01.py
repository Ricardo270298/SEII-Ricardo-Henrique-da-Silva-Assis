import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_arq = nome_do_arquivo_destino''
    new_arq = True
    while True:
        msg = s.recv(16)
        if new_arq:
            print("Tamanho do novo arquivo:",msg[:HEADERSIZE])
            arqlen = int(arq[:HEADERSIZE])
            new_arq = False



        full_arq += arq



        if len(full_arq)-HEADERSIZE == arqlen:

            pickle.loads(full_arq[HEADERSIZE:])
            new_arq = True
            full_arq = nome_do_arquivo_destino"
