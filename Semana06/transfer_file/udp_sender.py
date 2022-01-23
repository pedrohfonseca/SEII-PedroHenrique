# importando bibliotecas
import socket
import time
import sys

# definindo o ip, as portas de envio e o tamanho do buffer
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
# Recolhendo o nome do arquivo
file_name = sys.argv[1]


# Criando o socket para internet, com parâmetros de rede ip e protocolo udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Iniciando a conexão usando o ip e porta udp
sock.sendto(file_name.encode('utf-8'), (UDP_IP, UDP_PORT))
print ("Sending %s ..." % (file_name))

# Abrindo o arquivo como leitura
f = open(file_name, "r")
# # Lendo o que há no arquivo
data = f.read(buf)
while(data):
	# Enviando o dado para a porta
    if(sock.sendto(data.encode('utf-8'), (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Dê ao receptor um pouco de tempo para economizar

# Fechando o socket e o arquivo
sock.close()
f.close()
