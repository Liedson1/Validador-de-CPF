import socket

def cliente_tcp():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 65432))

    # Solicita o CPF do usuário
    cpf = input("\n=== Cliente TCP ===\nDigite o CPF ou 'STOP' para interromper o servidor: ")
    
    # Envia o CPF para o servidor
    client.sendall(cpf.encode())

    if cpf == "STOP":
        # Se for 'STOP', espera a confirmação de que o servidor foi fechado
        resposta = client.recv(1024).decode()
        print("Resposta do servidor:", resposta)
    else:
        # Recebe a resposta do servidor
        resposta = client.recv(1024).decode()
        print("Resposta do servidor:", resposta)
    
    # Fecha a conexão com o servidor
    client.close()

if __name__ == "__main__":
    cliente_tcp()
