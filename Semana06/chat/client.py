import socket # Importando bibliotecas
import threading
import time

PORT = 5050 # Definindo porta
FORMATO = 'utf-8' # Formato das mensagens
SERVER = "127.0.1.1" # IP do servidor
ADDR = (SERVER, PORT) # Tupla do endereço

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criando socket padrão TCP
client.connect(ADDR) # Se conectando com o servidor

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode() # Recebe as mensagens
        mensagem_splitada = msg.split("=") # Separa a mensagem
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2]) # Exibe quem enviou e o conteúdo da mensagem

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO)) # Envia mensagem codificada para o servidor

def enviar_mensagem():
    mensagem = input() # Coleta mensagem do cliente
    enviar("msg=" + mensagem) # e envia

def enviar_nome():
    nome = input('Digite seu nome: ') # Coleta nome do cliente
    enviar("nome=" + nome) # e envia

def iniciar_envio():
    enviar_nome() # Envia o nome do cliente
    enviar_mensagem() # Envia mensagem do cliente

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens) # Thread para receber mensagens
    thread2 = threading.Thread(target=iniciar_envio) # Thread para enviar mensagens dos clientes
    
    # Iniciando threads
    thread1.start()
    thread2.start()

iniciar()
