import socket # Importando bibliotecas
import threading
import time

SERVER_IP = socket.gethostbyname(socket.gethostname()) # Criando IP baseado no host
PORT = 5050 # Definindo porta
ADDR = (SERVER_IP, PORT) # Tupla do endereço
FORMATO = 'utf-8' # Formato das mensagens

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando socket padrão TCP
server.bind(ADDR) # Vinculando com o endereço

conexoes = [] # Listas para conexões e mensagens
mensagens = []

def enviar_mensagem_individual(conexao):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)): # Vai enviar as mensagens desde a ultima recebida até a quantidade total
        mensagem_de_envio = "msg=" + mensagens[i] # Concatena a mensagem com o inicio "msg="
        conexao['conn'].send(mensagem_de_envio.encode()) # Envia a mensagem para a conexão
        conexao['last'] = i + 1 # Atualiza a última mensagem enviada
        time.sleep(0.2) # Espera um pouco antes de enviar a próxima

def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes: # Enviando a mensagem individual para cada conexão, tornando para todos
        enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}") # Nova conexão criada
    global conexoes # Variáveis globais
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO) # Mensagem recebida é decodificada e armazenada
        if(msg):
            if(msg.startswith("nome=")): # Se a mensagem começar com "nome=", armazenaremos o nome
                mensagem_separada = msg.split("=") # mensagem é separada
                nome = mensagem_separada[1] # armezanado o nome para a conexão
                mapa_da_conexao = { # mapa com informações do cliente
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao) # mapa do novo cliente adicionado as conexões
                enviar_mensagem_individual(mapa_da_conexao) # Recebe mensagens antigas
            elif(msg.startswith("msg=")): # Se a mensagem começa com "msg=", temos uma nova mensagem
                mensagem_separada = msg.split("=") # mensagem é separada
                mensagem = nome + "=" + mensagem_separada[1] # armazenando a mensagem
                mensagens.append(mensagem) # adicionando as mensagens
                enviar_mensagem_todos() # envia mensagem para todos



def start():
    print("[INICIANDO] Iniciando Socket") # Iniciando o socket
    server.listen() # Socket começa a ouvir
    while(True):
        conn, addr = server.accept() # Quando ouver conexão, ele armazena o socket e o enredeço
        thread = threading.Thread(target=handle_clientes, args=(conn, addr)) # Cria uma thread para a conexão 
        thread.start() # Inicia a thread

start()
