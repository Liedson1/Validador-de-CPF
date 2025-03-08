import socket

def cliente_tcp():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 65432))

    
    cpf = input("\n=== Cliente TCP ===\nDigite o CPF ou 'STOP' para interromper o servidor: ")
    
    
    client.sendall(cpf.encode())

    if cpf == "STOP":
        
        resposta = client.recv(1024).decode()
        print("Resposta do servidor:", resposta)
    else:
        
        resposta = client.recv(1024).decode()
        print("Resposta do servidor:", resposta)
    
    
    client.close()

if __name__ == "__main__":
    cliente_tcp()
