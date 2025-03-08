import socket

def cliente_udp():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Solicita o CPF do usuário
    cpf = input("\n=== Cliente UDP ===\nDigite o CPF ou 'STOP' para interromper o servidor: ")
    
    # Envia o CPF para o servidor
    client.sendto(cpf.encode(), ("localhost", 65435))  # Envia para o servidor na porta 65433
    
    if cpf == "STOP":
        # Se for 'STOP', espera a confirmação de que o servidor foi fechado
        resposta, addr = client.recvfrom(1024)
        print("Resposta do servidor:", resposta.decode())
    else:
        # Recebe a resposta do servidor
        resposta, addr = client.recvfrom(1024)  # Utiliza recvfrom em vez de recv, já que é UDP
        print("Resposta do servidor:", resposta.decode())
    
    # Fecha o socket do cliente
    client.close()

if __name__ == "__main__":
    cliente_udp()
