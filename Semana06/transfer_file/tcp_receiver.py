# importando bibliotecas
import socket

# definindo o ip, as portas de envio e recepção, o tempo limite e o tamanho do buffer
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006
timeout = 3
buf = 1024

# Criando o socket para internet, com parâmetros de rede ip e protocolo tcp
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando ao ip e a porta de recebimento do nome do arquivo
sock_f.bind((TCP_IP, FILE_PORT))
# Escutando um de cada vez
sock_f.listen(1)

# Criando o socket para internet, com parâmetros de rede ip e protocolo tcp
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Vinculando ao ip e a porta de recebimento do dado
sock_d.bind((TCP_IP, DATA_PORT))
# Escutando um de cada vez
sock_d.listen(1)


while True:
	# Conexão aceita com o socket do envio de nome do arquivo
	# retornando o socket e o endereço vinculado
    conn, addr = sock_f.accept()
    # Recebe o buffer e armazena em data
    data = conn.recv(buf).decode()
    # Se tiver algo, printa o nome do arquivo
    if data:
        print ("File name:", data)
        # Retirando espaços no inicio e fim
        file_name = 'novo_' + data.strip()

	# Abrindo o arquivo como escrita
    f = open(file_name, 'wb')

	# Conexão aceita com o socket do envio de dados
	# retornando o socket e o endereço vinculado
    conn, addr = sock_d.accept()
    while True:
    	# Recebe os dados e escreve em um arquivo
        data = conn.recv(buf).decode()
        if not data:
            break
        f.write(data.encode('utf-8'))

	# Finaliza a escrita e fecha o arquivo
    print ("%s Finish!" % file_name)
    f.close()
