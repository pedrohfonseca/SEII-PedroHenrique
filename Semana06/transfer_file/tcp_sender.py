# importando bibliotecas
import socket
import sys

# definindo o ip, as portas de envio de dado e do nome do arquivo e recepção e o tamanho do buffer
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
buf = 1024
# Recolhendo o nome do arquivo
file_name = sys.argv[1]


try:
	# Criando o socket para internet, com parâmetros de rede ip e protocolo tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Iniciando a conexão usando o ip e porta de envio de arquivo
    sock.connect((TCP_IP, FILE_PORT))
    # Enviando o nome do arquivo
    sock.send(file_name.encode('utf-8'))
    # Fechando a conexão
    sock.close()

    print ("Sending %s ..." % (file_name))

	# Abrindo o arquivo como leitura
    f = open(file_name, "rb")
    # Abrindo novamente a conexão
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Iniciando a conexão usando o ip e porta de envio de dado
    sock.connect((TCP_IP, DATA_PORT))
	# Lendo o que há no arquivo
    data = f.read()
    # Enviando o conteúdo do arquivo
    sock.send(data)

finally:
	# Fechando a conexão e o arquivo
    sock.close()
    f.close()
