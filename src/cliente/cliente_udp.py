import socket

def cliente_udp():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    
    cpf = input("\n=== Cliente UDP ===\nDigite o CPF ou 'STOP' para interromper o servidor: ")
    
    
    client.sendto(cpf.encode(), ("localhost", 65435))  
    
    if cpf == "STOP":
        
        resposta, addr = client.recvfrom(1024)
        print("Resposta do servidor:", resposta.decode())
    else:
        
        resposta, addr = client.recvfrom(1024)
        print("Resposta do servidor:", resposta.decode())
    
   
    client.close()

if __name__ == "__main__":
    cliente_udp()
