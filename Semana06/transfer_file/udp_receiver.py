# importando bibliotecas
import socket
import select

# definindo o ip, as portas de envio e o tempo limite
UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3

# Criando o socket para internet, com parâmetros de rede ip e protocolo udp
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Vinculando ao ip e a porta de recebimento do nome do arquivo
sock.bind((UDP_IP, IN_PORT))

while True:
	# Recebendo dados de 1024 bytes. Retornando o dado e o endereço de origem
    data, addr = sock.recvfrom(1024)
    if data:
    	# Printando o nome do arquivo recebido
        print ("File name: ", data)
        # Retirando espaços no inicio e fim
        file_name = 'novo_' + data.strip().decode()

	# Abrindo arquivo no modo de escrita
    f = open(file_name, 'wb')

    while True:
    	# Espera até estar pronto para a leitura
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
        	# Se existir, recebe a quantidade de dado e escreve no arquivo
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
        	# Se não existir, finaliza e fecha o arquivo
            print ("%s Finish!" % (file_name))
            f.close()
            break
