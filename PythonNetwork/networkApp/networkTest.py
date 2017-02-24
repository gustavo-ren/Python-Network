'''
Created on 02 de fev de 2017

@author: Gustavo
'''
'''importacao do socket'''
import socket


'''cria um objeto socket, AF_INET para IPV4, SOCK_STREAM para comunicacao TCP'''
sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

'''outras opcoes seriam AF_INET6 pra IPV6 e SOCK_DGRAM para UDP
'''

'''Definicao de host e porta'''
HOST=''
PORT=5000

'''Realiza a conexao entre socket e endereco'''
sock.bind((HOST, PORT))

'''Bloqueia o socket, e o coloca em modo de epera por conexao.'''
sock.listen(1)
'''O numero entre parenteses mostra quantas conexoes o socket aceita enquanto esta esperando por conexao.'''

'''
conn e um novo objeto socket, especifico para a conexao do cliente, o socket sock serve para o servidor ouvir
addr possui as informacoes de endereco do cliente
.accept() cuida da negociacao de conexao, e os dados podem comecar a trafegar. 
'''
conn, addr= sock.accept()

conn.recv(1024)

conn.close()
sock.close()